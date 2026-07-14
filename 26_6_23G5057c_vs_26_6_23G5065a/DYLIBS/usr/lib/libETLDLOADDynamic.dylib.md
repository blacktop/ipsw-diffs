## libETLDLOADDynamic.dylib

> `/usr/lib/libETLDLOADDynamic.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`

```diff

-  __TEXT.__text: 0x152c
+  __TEXT.__text: 0x14b0
   __TEXT.__auth_stubs: 0x110
-  __TEXT.__cstring: 0x487
+  __TEXT.__cstring: 0x486
   __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x80
Functions:
~ _ETLDLOADCommandSend : 264 -> 240
~ _ETLDLOADCommandReceiveSmallWithFlags : 296 -> 272
~ _ETLDLOADCommandReceiveWithBufferAndFlags : 164 -> 140
~ _ETLDLOADDetectProtocolVersion : 840 -> 788
```
