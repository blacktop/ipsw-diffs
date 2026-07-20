## libARI.dylib

> `/usr/lib/libARI.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`

```diff

-1636.0.0.0.0
-  __TEXT.__text: 0x2067d4
+1638.0.0.0.0
+  __TEXT.__text: 0x206a84
   __TEXT.__init_offsets: 0x8
   __TEXT.__const: 0x15290
-  __TEXT.__gcc_except_tab: 0x1ab20
-  __TEXT.__cstring: 0x3e32b
+  __TEXT.__gcc_except_tab: 0x1ab64
+  __TEXT.__cstring: 0x3e38b
   __TEXT.__oslogstring: 0x4499
   __TEXT.__unwind_info: 0xdb68
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x46698
+  __DATA_CONST.__const: 0x46718
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x2a3b0

   - /usr/lib/libc++.1.dylib
   Functions: 17218
   Symbols:   24239
-  CStrings:  9458
+  CStrings:  9462
 
Functions:
~ __ZN6AriSdk38ARI_IBICallPsLTEAttachApnConfigReq_SDKD2Ev : 1924 -> 2004
~ __ZN6AriSdk38ARI_IBICallPsLTEAttachApnConfigReq_SDK4packEPP6AriMsg : 3136 -> 3264
~ __ZN6AriSdk38ARI_IBICallPsLTEAttachApnConfigReq_SDK6unpackEv : 12116 -> 12596
CStrings:
+ "is_always_on_home1_t135"
+ "is_always_on_home2_t136"
+ "is_always_on_roam1_t137"
+ "is_always_on_roam2_t144"
```
