## Diagnostic-3939

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3939.appex/Diagnostic-3939`

```diff

-1066.0.41.0.0
-  __TEXT.__text: 0x74b4
+1066.0.73.0.0
+  __TEXT.__text: 0x74c0
   __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_stubs: 0x1860
+  __TEXT.__objc_stubs: 0x18c0
   __TEXT.__objc_methlist: 0xa44
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x288
+  __TEXT.__gcc_except_tab: 0x290
   __TEXT.__cstring: 0x32c
-  __TEXT.__objc_methname: 0x1d61
-  __TEXT.__oslogstring: 0x3cc
+  __TEXT.__objc_methname: 0x1d69
+  __TEXT.__oslogstring: 0x3ad
   __TEXT.__objc_classname: 0x1ac
-  __TEXT.__objc_methtype: 0x59b
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__objc_methtype: 0x582
+  __TEXT.__unwind_info: 0x228
   __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0x2d8
   __DATA_CONST.__cfstring: 0x820
   __DATA_CONST.__objc_classlist: 0x88

   __DATA_CONST.__objc_intobj: 0x2a0
   __DATA_CONST.__objc_doubleobj: 0x70
   __DATA.__objc_const: 0x16a0
-  __DATA.__objc_selrefs: 0x808
+  __DATA.__objc_selrefs: 0x820
   __DATA.__objc_ivar: 0xd8
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 09A88E87-F04D-3902-9B90-C1D16153A976
+  UUID: 3B630D54-64E3-369D-8E6F-9DCA9C1C2202
   Functions: 219
-  Symbols:   182
-  CStrings:  625
+  Symbols:   183
+  CStrings:  628
 
Symbols:
+ _OBJC_CLASS_$_NSLock
Functions:
~ sub_100004464 : 2772 -> 2776
~ sub_100006170 -> sub_100006174 : 316 -> 336
~ sub_1000078b8 -> sub_1000078d0 : 1036 -> 1048
~ sub_100007cc4 -> sub_100007ce8 : 184 -> 160
CStrings:
+ "@\"NSLock\""
+ "Haptic engine stopped for reason %ld"
+ "Haptic playback timed out"
+ "T@\"NSLock\",&,N,V_hapticPlaybackLock"
+ "_hapticPlaybackLock"
+ "dateWithTimeIntervalSinceNow:"
+ "hapticPlaybackLock"
+ "lockBeforeDate:"
+ "setHapticPlaybackLock:"
+ "unlock"
- "@\"NSObject<OS_dispatch_semaphore>\""
- "Failed to signal playback semaphore while playing haptic."
- "Haptic engine stoped for reason %ld"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_hapticPlaybackSemaphore"
- "_hapticPlaybackSemaphore"
- "hapticPlaybackSemaphore"
- "setHapticPlaybackSemaphore:"

```
