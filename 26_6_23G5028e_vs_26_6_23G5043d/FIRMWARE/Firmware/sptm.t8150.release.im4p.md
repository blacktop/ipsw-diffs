## sptm.t8150.release.im4p

> `Firmware/sptm.t8150.release.im4p`

```diff

-611.160.8.0.0
-  __TEXT.__cstring: 0x12429 sha256:53559faec38820c0618b7a0dfa6c157ad3e67996769cd097d84835682675a8f4
+611.160.16.0.0
+  __TEXT.__cstring: 0x12639 sha256:70a7c3a4349d12a98db92f8bad85fffbd79a3e4ab55850cab0df07887176ade0
   __TEXT.__const: 0xa80 sha256:86e4e0231f2196f0d5cc0718fa9ce845038dd2a97c4ebe9e2cdbb3fe16680469
   __TEXT.__binname: 0x40 sha256:9b8687df57d1255032e0cd6cb11d3adf1f66c5728445d93663e9127250a426e9
   __TEXT.__chain_starts: 0x24 sha256:5fd465bdb02cb78c99c9e28360e580ee08c868d6e85ab4d384c856b07862a8c8
-  __DATA_CONST.__const: 0x5c98 sha256:f9316a2b52dbbb0d0beb374ff45ddb12db1732577763c6daa9e7279ede20d052
-  __LATE_CONST.__late_const: 0x7c1f0 sha256:1fe0c47e8396facdeb4a422178fa0eae77d89a5c74291d1f596e09f3a8d6aeff
-  __TEXT_EXEC.__text: 0x5ef6c sha256:6e8dab7b75a0a9f905e79651caf3aff5b8c0c83470938772e84c8f2f0acd585b
+  __DATA_CONST.__const: 0x5ca8 sha256:cc38444bde689368c702033501ff9d21cff323859cbf8735d60ffead5d35ba44
+  __LATE_CONST.__late_const: 0x7c1f0 sha256:d0fb10e18e492d380354e27958e72ca0297f6097ac84da3d97e063057207d734
+  __TEXT_EXEC.__text: 0x5f754 sha256:08a038687bf1770dd7d86cad70c911d053bf7f3c4f0ae8194ce3ed516e9c5bee
   __LAST.__pinst: 0x8 sha256:fbfe010a65f336a0c74a09adf932e560cbf8dd3dc61641cea7abbff4f544861d
   __DATA.__data: 0xf sha256:19e4507360b4447be5d0e175ca4c36014495cca39af824ef7eb39a42e51890dc
   __DATA.__auth_ptr: 0x18 sha256:51cc4b60c729ed443403a90b873ec70dcaebf406636b31a52c61107ce5ec5ce4
   __DATA.__bss: 0x60a8 sha256:1fb054d6fb6753955be0031a1fda9d77d3af0de3bc4ec8f1ec6479b381d22067
   __DATA.__common: 0x8608 sha256:cf6b19b2d82778866b6491eb6edf4e28d4ee82a3cddfe321e7dbd82368e3341c
   __BOOTDATA.__data: 0x14000 sha256:fa569e2360c540e6280e34a4627516770f1a5f34d81d35689334a99cc1013357
-  UUID: 5967F76F-5229-3007-BA12-8A47EA8219E0
-  Functions: 392
+  UUID: F9CC9422-820B-3E16-8D85-C925951E7ADF
+  Functions: 393
   Symbols:   1
-  CStrings:  2307
+  CStrings:  2317
 
CStrings:
+ "%s: assert '!__builtin_add_overflow(cputrace_instance->initialized_count, 1, &cputrace_instance->initialized_count)' failed."
+ "%s: assert '!__builtin_sub_overflow(cputrace_instance->initialized_count, 1, &cputrace_instance->initialized_count)' failed."
+ "%s: assert 'cluster_id < CPUTRACE_NB_CLUSTERS' failed."
+ "%s: cluster not deinitialized before hibernating."
+ "%s: clusters not deinitialized before hibernating."
+ "SPTM-611.160.16|2026-06-07:19:11:09.005300|"
+ "VIOLATION_CPUTRACE_VA_DEINITIALIZED"
+ "VIOLATION_CPUTRACE_VA_INITIALIZED"
+ "cputrace_get_cluster_id()"
+ "cputrace_instance->initialized_count"
+ "relaxed-rw-protections"
+ "sptm_cputrace_hib_wake"
- "%s: assert 'cluster_id <= MAX_CPU_CLUSTER_PHY_ID' failed."
- "SPTM-611.160.8|2026-05-14:23:21:13.337295|"

```
