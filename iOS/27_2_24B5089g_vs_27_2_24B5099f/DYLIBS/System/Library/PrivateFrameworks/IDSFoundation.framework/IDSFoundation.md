## IDSFoundation

> `/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation`

```diff

-2003.200.44.0.0
-  __TEXT.__text: 0x4e1dc4
-  __TEXT.__objc_methlist: 0x1bf64
+2003.200.61.0.0
+  __TEXT.__text: 0x4e2e0c
+  __TEXT.__objc_methlist: 0x1bfdc
   __TEXT.__const: 0x406f0
-  __TEXT.__cstring: 0x35c1d
-  __TEXT.__oslogstring: 0x2cf7a
+  __TEXT.__cstring: 0x35dad
+  __TEXT.__oslogstring: 0x2d0ba
   __TEXT.__gcc_except_tab: 0xc018
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x188

   __TEXT.__swift5_acfuncs: 0x1cc
   __TEXT.__swift5_mpenum: 0x164
   __TEXT.__swift5_types2: 0x20
-  __TEXT.__unwind_info: 0x1a308
-  __TEXT.__eh_frame: 0x1679c
+  __TEXT.__unwind_info: 0x19e60
+  __TEXT.__eh_frame: 0x167cc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x76d0
-  __DATA_CONST.__objc_classlist: 0x12c0
+  __DATA_CONST.__const: 0x76e8
+  __DATA_CONST.__objc_classlist: 0x12c8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb310
+  __DATA_CONST.__objc_selrefs: 0xb350
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0xb30
+  __DATA_CONST.__objc_superrefs: 0xb38
   __DATA_CONST.__objc_arraydata: 0x1558
-  __DATA_CONST.__got: 0x1530
-  __AUTH_CONST.__const: 0x1ab58
-  __AUTH_CONST.__cfstring: 0x2d4c0
-  __AUTH_CONST.__objc_const: 0x3f0d8
-  __AUTH_CONST.__objc_intobj: 0xc48
+  __DATA_CONST.__got: 0x1570
+  __AUTH_CONST.__const: 0x1abb8
+  __AUTH_CONST.__cfstring: 0x2d680
+  __AUTH_CONST.__objc_const: 0x3f250
+  __AUTH_CONST.__objc_intobj: 0xc78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x1e90
-  __AUTH_CONST.__auth_got: 0x2a60
-  __AUTH.__objc_data: 0xa468
+  __AUTH_CONST.__auth_got: 0x2a68
+  __AUTH.__objc_data: 0xa4b8
   __AUTH.__data: 0xafd8
-  __DATA.__objc_ivar: 0x28f8
+  __DATA.__objc_ivar: 0x2914
   __DATA.__data: 0xf580
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x220
   __DATA_DIRTY.__objc_data: 0x14f0
   __DATA_DIRTY.__data: 0x1f8
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libtailspin.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 32051
-  Symbols:   5113
-  CStrings:  8493
+  Functions: 32071
+  Symbols:   5129
+  CStrings:  8514
 
Symbols:
+ _IDSGroupSessionInEndpointContextDataKey
+ _IDSGroupSessionInviteDeclineReasonKey
+ _IDSSessionRemoteDestinationSameAccountKey
+ _OBJC_CLASS_$_IDSTailspinCapture
+ _OBJC_METACLASS_$_IDSTailspinCapture
+ _TSPDumpOptions_CollectAriadnePlists
+ _TSPDumpOptions_CollectOsLogs
+ _TSPDumpOptions_CollectOsSignposts
+ _TSPDumpOptions_CollectTrials
+ _TSPDumpOptions_MinTraceBufferDurationSec
+ _TSPDumpOptions_ReasonString
+ _TSPDumpOptions_ScrubOutput
+ _TSPDumpOptions_Symbolicate
+ _TSPDumpOptions_TargetPID
+ _os_unfair_lock_trylock
+ _tailspin_dump_output_with_options_sync
CStrings:
+ "%@_%@.tailspin"
+ ".tailspin"
+ "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
+ "B"
+ "IDS detected issue with %@"
+ "IDSTailspinCapture: dump failed for %{public}@ after %.2fs"
+ "IDSTailspinCapture: failed to create %{public}@: %{errno}d. Suppressing further open failures."
+ "IDSTailspinCapture: saved %{public}@ in %.2fs"
+ "IDSTailspinCapture: unable to create %{public}@: %{public}@"
+ "IDSTailspinCapture: unable to remove %{public}@: %{public}@"
+ "IDSTailspinCaptureEnabled"
+ "IDSTailspinCaptureMinRestSeconds"
+ "Library/IdentityServices/Tailspins"
+ "Notes Voicenotes"
+ "com.apple.private.alloy.notes.voicenotes"
+ "en_US_POSIX"
+ "gs-invite-decline-reason-key"
+ "ids.tailspin"
+ "in-endpoint-context-data-key"
+ "remote-destination-same-account"
+ "yyyyMMdd_HHmmss"
```
