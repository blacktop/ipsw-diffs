## libenergytrace.dylib

> `/usr/lib/libenergytrace.dylib`

```diff

 23.0.0.0.0
-  __TEXT.__text: 0x694 sha256:c15797586b8fceba62819ce476aa057639fa5397295f292bfceb09deb09ccdab
-  __TEXT.__auth_stubs: 0x70 sha256:32a2437b927c47bc26b83d8ea65dad41314c1d85e57d57e7ed1622eb2d786182
+  __TEXT.__text: 0x5d8 sha256:d99e9fcaa684497a6f7934ba761d7b631865c165a69baf7ee2c1bb9103fb490e
   __TEXT.__const: 0x10 sha256:aba2c3d2096ba933e75011352adad082c5f240df3c2ca01646fd8bfa24d54a32
   __TEXT.__oslogstring: 0x19f sha256:7a84f40cff6d784b7e0ed3771381add5e8a9de7713afb04cdb92ab8295bebe66
   __TEXT.__cstring: 0x57 sha256:ca07812bfee4f05a38739cc6b57330057fc14ef94af1c84fd85d5ff417fe8b49
-  __TEXT.__unwind_info: 0x88 sha256:8a901110a12541fe2239dfd22280be9394cc8aba608747f35254580a6c1cb15c
-  __DATA_CONST.__got: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __DATA_CONST.__const: 0x20 sha256:9b5936c0734e4bff38e3b2e4ee34fd319feb52761c597696573cbc930a3aa5c9
-  __AUTH_CONST.__auth_got: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
-  __AUTH_CONST.__const: 0x20 sha256:b5009836aa053db6cbba2c0e8ebbc5c9fc4ca2d5bdef85386dc58a36e7a2c210
+  __TEXT.__unwind_info: 0x80 sha256:9421ec22fc0ad856eba66cae5c9eff22efcfe64fbc7eda143f3028d04c18fffe
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x20 sha256:e842f40fed7765b9dce8c2d1e3f72b60789ebd203acbd38d3879c65c445880d8
+  __AUTH_CONST.__const: 0x20 sha256:bcdc6c56d034b9beca83070d846dfd2a8c6feca4fdcc23475b5d25445143338c
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__bss: 0x48 sha256:834a709ba2534ebe3ee1397fd4f7bd288b2acc1d20a08d6c862dcd99b6f04400
   - /usr/lib/libSystem.B.dylib
-  UUID: 75320403-56D3-31FE-BD5B-04B32719AC17
+  UUID: 3C822BE3-58EF-3680-9554-40A957348CC7
   Functions: 11
-  Symbols:   28
+  Symbols:   26
   CStrings:  12
 
Symbols:
- ___stack_chk_fail
- ___stack_chk_guard
Functions:
~ __get_signpost_params.cold.1 -> _entr_act_modify : 20 -> 248
~ _entr_act_begin -> __get_signpost_params : 296 -> 160
~ __get_signpost_params -> _entr_act_begin : 160 -> 252
~ _entr_act_end : 296 -> 252
~ ____get_signpost_params_block_invoke -> __get_signpost_params.cold.1 : 124 -> 20
~ _entr_act_modify -> _entr_act_set : 292 -> 8
~ _entr_shouldtrace -> ____get_signpost_params_block_invoke : 116 -> 124
~ _entr_act_set -> _entr_shouldtrace : 8 -> 104
~ _entr_event : sha256 e431dcb2ef3158c468178822e60207903ea0655e994017a8a87fe5ec9fc76c5d -> 28509154002f5d12c992762b5b849a8dedd71b6e38a381b46c8cdfc7362ce6e6
~ _entr_act_associate : 320 -> 276
~ _entr_act_setd : sha256 4d34671ba3aab075f26175ec48a23ba318ab6e2f974cf2b1c6c8ae28ce9915fa -> 7186295616952191ea64d65cdbba718fcb8b2eb1d13d326763fb6d15dded159a

```
