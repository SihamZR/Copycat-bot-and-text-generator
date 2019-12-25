#!/usr/bin/env python3

import json
import os
import numpy as np
import tensorflow as tf

import app.AI.GenText.model as model
import app.AI.GenText.sample as sample
import app.AI.GenText.encoder as encoder

def interact_model(summary,nsamples=1,batch_size=1,length=400):
    
    model_name='774M'
    seed=None
    temperature=1
    top_k=40
    top_p=1
    models_dir='D:\Projects\contentGen\\app\AI\models'



    outputdir=os.path.expanduser(os.path.expandvars('result'))
    models_dir = os.path.expanduser(os.path.expandvars(models_dir))
    if batch_size is None:
        batch_size = 1
    assert nsamples % batch_size == 0

    enc = encoder.get_encoder(model_name, models_dir)
    hparams = model.default_hparams()
    with open(os.path.join(models_dir, model_name, 'hparams.json')) as f:
        hparams.override_from_dict(json.load(f))

    if length is None:
        length = hparams.n_ctx // 2
    elif length > hparams.n_ctx:
        raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

    with tf.Session(graph=tf.Graph()) as sess:
        context = tf.placeholder(tf.int32, [batch_size, None])
        np.random.seed(seed)
        tf.set_random_seed(seed)
        output = sample.sample_sequence(
            hparams=hparams, length=length,
            context=context,
            batch_size=batch_size,
            temperature=temperature, top_k=top_k, top_p=top_p
        )

        saver = tf.train.Saver()
        ckpt = tf.train.latest_checkpoint(os.path.join(models_dir, model_name))
        saver.restore(sess, ckpt)

        raw_text = summary
        context_tokens = enc.encode(raw_text)
        generated = 0
        for _ in range(nsamples // batch_size):
            out = sess.run(output, feed_dict={
                context: [context_tokens for _ in range(batch_size)]
            })[:, len(context_tokens):]
            outSamples = []
            for i in range(batch_size):
                generated += 1
                text = enc.decode(out[i])
                outSamples.append(text)
                #print("=" * 40 + " SAMPLE " + str(generated) + " " + "=" * 40)
                #print(text)
        #print("=" * 80)
        return outSamples


