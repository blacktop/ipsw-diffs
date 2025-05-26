## TimeSync

> `/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync`

```diff

-1220.2.0.0.0
-  __TEXT.__text: 0x6dfe0
+1230.2.0.0.0
+  __TEXT.__text: 0x6e22c
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_methlist: 0x71c4
+  __TEXT.__objc_methlist: 0x7224
   __TEXT.__oslogstring: 0x6038
-  __TEXT.__cstring: 0x7107
+  __TEXT.__cstring: 0x7227
   __TEXT.__const: 0x160
-  __TEXT.__gcc_except_tab: 0x178c
-  __TEXT.__unwind_info: 0x1e68
+  __TEXT.__gcc_except_tab: 0x1884
+  __TEXT.__unwind_info: 0x1e98
   __TEXT.__eh_frame: 0x4c
-  __TEXT.__objc_classname: 0xd67
-  __TEXT.__objc_methname: 0xb736
-  __TEXT.__objc_methtype: 0x1bde
-  __TEXT.__objc_stubs: 0x7360
+  __TEXT.__objc_classname: 0xd66
+  __TEXT.__objc_methname: 0xb816
+  __TEXT.__objc_methtype: 0x1c33
+  __TEXT.__objc_stubs: 0x73e0
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x1020
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xdd88
-  __DATA_CONST.__objc_selrefs: 0x2320
+  __DATA_CONST.__objc_const: 0xdd48
+  __DATA_CONST.__objc_selrefs: 0x2358
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__cfstring: 0x4f80
   __AUTH_CONST.__objc_intobj: 0x30

   __DATA.__objc_protorefs: 0xa0
   __DATA.__objc_classrefs: 0x3d8
   __DATA.__objc_superrefs: 0x3d8
-  __DATA.__objc_ivar: 0xa44
+  __DATA.__objc_ivar: 0xa34
   __DATA.__data: 0xb48
   __DATA.__bss: 0x88
   __DATA_DIRTY.__const: 0x5a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2837
-  Symbols:   9012
-  CStrings:  3367
+  Functions: 2845
+  Symbols:   9033
+  CStrings:  3383
 
Symbols:
+ -[TSDCKernelClock getUpdateLock]
+ -[TSDCKernelClock internalLockState]
+ -[TSDCKernelClock setInternalLockState:]
+ -[TSDCKernelClock setTranslationClock:]
+ -[TSDCKernelClock setUpdateLock:]
+ -[TSDCKernelClock setValidIndex:]
+ -[TSDCKernelClock translationClock]
+ -[TSDCKernelClock updateLock]
+ -[TSDCKernelClock validIndex]
+ _objc_msgSend$getUpdateLock
+ _objc_msgSend$internalLockState
+ _objc_msgSend$setInternalLockState:
+ _objc_msgSend$setValidIndex:
+ _objc_msgSend$validIndex
- -[TSDCKernelClock getValidIndex]
- _OBJC_IVAR_$_TSDCgPTPClock._internalLockState
- _OBJC_IVAR_$_TSDCgPTPClock._translationClock
- _OBJC_IVAR_$_TSDCgPTPClock._updateLock
- _OBJC_IVAR_$_TSDCgPTPClock._validIndex
- _objc_msgSend$getValidIndex
CStrings:
+ "\x01\xf0\xf0\xf0\xf0A\x11"
+ "T@\"TSClock\",&,N,V_translationClock"
+ "TI,N,V_validIndex"
+ "Ti,N,V_internalLockState"
+ "T{os_unfair_lock_s=I},N,V_updateLock"
+ "[self.translationClock getMachAbsoluteRateRatioNumerator:&machNumer denominator:&machDenom machAnchor:nil andDomainAnchor:nil withError:nil]"
+ "[self.translationClock getTimeSyncTimeRateRatioNumerator:&transNumer denominator:&transDenom timeSyncAnchor:nil andDomainAnchor:nil withError:nil]"
+ "^{os_unfair_lock_s=I}16@0:8"
+ "getUpdateLock"
+ "internalLockState"
+ "setInternalLockState:"
+ "setTranslationClock:"
+ "setUpdateLock:"
+ "setValidIndex:"
+ "updateLock"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "validIndex"
+ "{os_unfair_lock_s=I}16@0:8"
+ "\xf0\xf0\"B"
+ "\xf0\xf0\xa1"
- "\x01\xf0\xf0\xf0\xf0R!"
- "getValidIndex"
- "\xf0\xf0!\x12A"
- "\xf0\xf0\xb1"

```
