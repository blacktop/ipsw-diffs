## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-240.6.1.0.0
-  __TEXT.__text: 0x1c2c08
+250.7.1.0.0
+  __TEXT.__text: 0x1c2b40
   __TEXT.__auth_stubs: 0x1f40
-  __TEXT.__objc_methlist: 0x4d5c
+  __TEXT.__objc_methlist: 0x4d6c
   __TEXT.__cstring: 0x2a246
   __TEXT.__const: 0x1af8
-  __TEXT.__gcc_except_tab: 0x1f98
-  __TEXT.__oslogstring: 0x3535e
+  __TEXT.__gcc_except_tab: 0x1fa0
+  __TEXT.__oslogstring: 0x35370
   __TEXT.__dlopen_cstrs: 0x5bd
-  __TEXT.__unwind_info: 0x4468
+  __TEXT.__unwind_info: 0x4470
   __TEXT.__objc_classname: 0x506
-  __TEXT.__objc_methname: 0x12a21
-  __TEXT.__objc_methtype: 0x1c8b
+  __TEXT.__objc_methname: 0x12a86
+  __TEXT.__objc_methtype: 0x1c96
   __TEXT.__objc_stubs: 0xb6c0
   __DATA_CONST.__got: 0xa18
   __DATA_CONST.__const: 0x6408

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3378
   __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0xfb8
   __AUTH_CONST.__const: 0x3b58
   __AUTH_CONST.__cfstring: 0x17800
-  __AUTH_CONST.__objc_const: 0x74f8
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_const: 0x7528
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x500
   __AUTH.__data: 0x510
-  __DATA.__objc_ivar: 0x758
+  __DATA.__objc_ivar: 0x75c
   __DATA.__data: 0xf2c
   __DATA.__bss: 0x15d8
-  __DATA.__common: 0x500
+  __DATA.__common: 0x4f0
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x4e8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 15F78A5A-FA94-3F0C-BB4A-0E3E26E38AB3
-  Functions: 5917
-  Symbols:   19776
-  CStrings:  13161
+  UUID: BF9C1FD4-FA04-351F-8405-EE351BBD1510
+  Functions: 5918
+  Symbols:   19780
+  CStrings:  13164
 
Symbols:
+ +[MXSystemController(Common) copyMXSystemControllerList:]
+ -[MXSessionManager phoneCallIsAboutToGoActiveOverCarPlay]
+ -[MXSessionManager setPhoneCallIsAboutToGoActiveOverCarPlay:]
+ _IOHIDEventSystemClientSetMatchingMultiple
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_IVAR_$_MXSessionManager._phoneCallIsAboutToGoActiveOverCarPlay
+ _gMXSystemControllerListLock
+ _objc_msgSend$copyMXSystemControllerList:
+ _objc_msgSend$phoneCallIsAboutToGoActiveOverCarPlay
+ _objc_msgSend$setPhoneCallIsAboutToGoActiveOverCarPlay:
- +[MXSystemController(Common) mxSystemControllerListBeginIteration]
- +[MXSystemController(Common) mxSystemControllerListEndIteration]
- _IOHIDEventSystemClientSetMatching
- _gMXSystemControllerListActiveReaders
- _gMXSystemControllerListReadLock
- _gMXSystemControllerListWriteSemaphore
- _objc_msgSend$mxSystemControllerListBeginIteration
- _objc_msgSend$mxSystemControllerListEndIteration
- _objc_msgSend$numberWithInteger:
CStrings:
+ "-MXSystemSounds- %s: Applying scalar volume = %f for category = %{public}@ with max ssid volume = %f over rawVolume = %f"
+ "23:06:02"
+ "@20@0:8B16"
+ "Jun  3 2025"
+ "TB,N,V_phoneCallIsAboutToGoActiveOverCarPlay"
+ "_phoneCallIsAboutToGoActiveOverCarPlay"
+ "copyMXSystemControllerList:"
+ "phoneCallIsAboutToGoActiveOverCarPlay"
+ "setPhoneCallIsAboutToGoActiveOverCarPlay:"
- "-MXRoutingManager_AudioContext- %s: Sub endpoint info was not provided in the inFailureInfo dictionary"
- "01:55:59"
- "Apr 19 2025"
- "mxSystemControllerListBeginIteration"
- "mxSystemControllerListEndIteration"
- "numberWithInteger:"

```
