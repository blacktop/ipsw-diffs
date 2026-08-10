## NetworkQuality

> `/System/Library/PrivateFrameworks/NetworkQuality.framework/NetworkQuality`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-220.0.0.0.0
-  __TEXT.__text: 0x1fec0
-  __TEXT.__objc_methlist: 0x1d10
-  __TEXT.__const: 0x198
+224.0.0.0.0
+  __TEXT.__text: 0x201dc
+  __TEXT.__objc_methlist: 0x1d88
+  __TEXT.__const: 0x1a8
   __TEXT.__gcc_except_tab: 0x68c
-  __TEXT.__cstring: 0x2c3d
+  __TEXT.__cstring: 0x2c84
   __TEXT.__oslogstring: 0x2219
-  __TEXT.__unwind_info: 0x690
+  __TEXT.__unwind_info: 0x698
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1340
+  __DATA_CONST.__objc_selrefs: 0x1380
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__got: 0x208
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1de0
-  __AUTH_CONST.__objc_const: 0x4460
+  __AUTH_CONST.__cfstring: 0x1e60
+  __AUTH_CONST.__objc_const: 0x4550
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x510
+  __DATA.__objc_ivar: 0x524
   __DATA.__data: 0x360
   __DATA.__bss: 0x20
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 716
-  Symbols:   2043
-  CStrings:  572
+  Functions: 726
+  Symbols:   2066
+  CStrings:  576
 
Symbols:
+ -[NetworkQualityConfiguration commandLineArguments]
+ -[NetworkQualityConfiguration draftVersion]
+ -[NetworkQualityConfiguration intervalDuration]
+ -[NetworkQualityConfiguration maxProbesPerSecond]
+ -[NetworkQualityConfiguration setCommandLineArguments:]
+ -[NetworkQualityConfiguration setDraftVersion:]
+ -[NetworkQualityConfiguration setIntervalDuration:]
+ -[NetworkQualityConfiguration setMaxProbesPerSecond:]
+ -[NetworkQualityResult draftVersion]
+ -[NetworkQualityResult setDraftVersion:]
+ _OBJC_IVAR_$_NetworkQualityConfiguration._commandLineArguments
+ _OBJC_IVAR_$_NetworkQualityConfiguration._draftVersion
+ _OBJC_IVAR_$_NetworkQualityConfiguration._intervalDuration
+ _OBJC_IVAR_$_NetworkQualityConfiguration._maxProbesPerSecond
+ _OBJC_IVAR_$_NetworkQualityResult._draftVersion
+ _objc_msgSend$commandLineArguments
+ _objc_msgSend$draftVersion
+ _objc_msgSend$intervalDuration
+ _objc_msgSend$maxProbesPerSecond
+ _objc_msgSend$setCommandLineArguments:
+ _objc_msgSend$setDraftVersion:
+ _objc_msgSend$setIntervalDuration:
+ _objc_msgSend$setMaxProbesPerSecond:
CStrings:
+ "commandLineArguments"
+ "draftVersion"
+ "intervalDuration"
+ "maxProbesPerSecond"
```
