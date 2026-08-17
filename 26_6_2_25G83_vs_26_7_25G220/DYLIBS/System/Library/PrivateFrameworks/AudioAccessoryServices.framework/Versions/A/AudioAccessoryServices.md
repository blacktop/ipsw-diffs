## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/Versions/A/AudioAccessoryServices`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_classname`

```diff

 35.14.0.0.0
-  __TEXT.__text: 0x4a7a8
+  __TEXT.__text: 0x4a984
   __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_methlist: 0x599c
+  __TEXT.__objc_methlist: 0x59d4
   __TEXT.__const: 0x240
-  __TEXT.__gcc_except_tab: 0x16c8
-  __TEXT.__cstring: 0xc00c
+  __TEXT.__gcc_except_tab: 0x16d4
+  __TEXT.__cstring: 0xc030
   __TEXT.__unwind_info: 0x1608
   __TEXT.__objc_classname: 0x6ea
-  __TEXT.__objc_methname: 0xc4fe
+  __TEXT.__objc_methname: 0xc5f8
   __TEXT.__objc_methtype: 0x15b3
-  __TEXT.__objc_stubs: 0x6220
+  __TEXT.__objc_stubs: 0x6280
   __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x818
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2730
+  __DATA_CONST.__objc_selrefs: 0x2758
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x150
   __AUTH_CONST.__auth_got: 0x3c0
   __AUTH_CONST.__const: 0xc60
-  __AUTH_CONST.__cfstring: 0x2660
-  __AUTH_CONST.__objc_const: 0x9fd8
+  __AUTH_CONST.__cfstring: 0x26a0
+  __AUTH_CONST.__objc_const: 0xa068
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x958
+  __DATA.__objc_ivar: 0x964
   __DATA.__data: 0xcc8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xff0

   - /System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2466
-  Symbols:   4346
-  CStrings:  3917
+  Functions: 2471
+  Symbols:   4357
+  CStrings:  3932
 
Symbols:
+ -[AudioAccessoryDevice securePaired]
+ -[AudioAccessoryDevice securePairingCapability]
+ -[AudioAccessoryDevice secureSensorCapability]
+ -[AudioAccessoryDevice setSecurePaired:]
+ -[AudioAccessoryDevice setSecureSensorCapability:]
+ OBJC_IVAR_$_AudioAccessoryDevice._securePaired
+ OBJC_IVAR_$_AudioAccessoryDevice._securePairingCapability
+ OBJC_IVAR_$_AudioAccessoryDevice._secureSensorCapability
+ _objc_msgSend$secureSensorCapability
+ _objc_msgSend$setSecurePaired:
+ _objc_msgSend$setSecureSensorCapability:
CStrings:
+ "TB,N,V_securePaired"
+ "TC,N,V_secureSensorCapability"
+ "TC,R,N,V_securePairingCapability"
+ "_securePaired"
+ "_securePairingCapability"
+ "_secureSensorCapability"
+ "sccp"
+ "sec pr %u, "
+ "sec snsr %s, "
+ "securePaired"
+ "securePairingCapability"
+ "secureSensorCapability"
+ "setSecurePaired:"
+ "setSecureSensorCapability:"
+ "spmd"
+ "\xf0?"
- "\xf0/"
```
