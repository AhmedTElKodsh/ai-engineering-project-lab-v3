# Debug from evidence

Read the actual command, traceback/output and relevant code. State expected versus observed behavior. Identify the supported failing layer: import/configuration, provider/network, parse/schema, source support, retrieval, tool/scope, state or infrastructure.

Choose one small experiment that distinguishes the leading explanation from a plausible alternative. Do not prescribe retrying the provider for a local import error, or fix a retrieval miss by blindly rewriting the answer prompt. A service timeout is not confirmed not-found.

Make the smallest requested correction and verify the observation. Add a local regression case where useful. Record which part the learner diagnosed and which part the assistant supplied. Later assess a different failure for independent ownership; asking the learner to repeat the assistant's words is not independent diagnosis.

When exact evidence is missing, say what remains uncertain and request only the missing discriminating information. Do not invent a run, traceback, fixed result or saved checkpoint.
