## mobileactivationd

> `/usr/libexec/mobileactivationd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 1076.160.6.0.0
-  __TEXT.__text: 0x65438
+  __TEXT.__text: 0x6549c
   __TEXT.__auth_stubs: 0x1130
   __TEXT.__objc_stubs: 0x2480
   __TEXT.__objc_methlist: 0x8ec

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1434
+  Functions: 1433
   Symbols:   3443
   CStrings:  2454
 
Functions:
~ _OUTLINED_FUNCTION_11 : 16 -> 40
~ _OUTLINED_FUNCTION_12 : 40 -> 12
~ _OUTLINED_FUNCTION_13 : 12 -> 24
~ _OUTLINED_FUNCTION_15 : 24 -> 12
~ _OUTLINED_FUNCTION_16 : 12 -> 28
~ _OUTLINED_FUNCTION_18 : 28 -> 36
~ _OUTLINED_FUNCTION_19 : 36 -> 20
~ _OUTLINED_FUNCTION_21 : 20 -> 28
- _OUTLINED_FUNCTION_22
~ _serializeParameters : 276 -> 284
~ _DeserializeCredential : 436 -> 432
~ _LibSer_SEPControl_Deserialize : 156 -> 196
~ _LibSer_SEPControlResponse_Deserialize : 64 -> 88
~ _LibSer_ACMDeserializeEnvironmentVariableType : 140 -> 148
~ _LibSer_ACMDeserializeSEPControlCode : 268 -> 308
CStrings:
+ "Absinthe/2.0 macOS Device Activator (MobileActivation-1076.160.6 built on Jul 31 2026 at 21:25:48)"
- "Absinthe/2.0 macOS Device Activator (MobileActivation-1076.160.6 built on Jul 11 2026 at 17:50:21)"
```
