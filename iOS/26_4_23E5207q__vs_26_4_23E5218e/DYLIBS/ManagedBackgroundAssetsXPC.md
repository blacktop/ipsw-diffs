## ManagedBackgroundAssetsXPC

> `/System/Library/PrivateFrameworks/ManagedBackgroundAssetsXPC.framework/ManagedBackgroundAssetsXPC`

```diff

-1.4.9.0.0
-  __TEXT.__text: 0x2ac14
-  __TEXT.__auth_stubs: 0x10e0
+1.4.13.0.0
+  __TEXT.__text: 0x2b42c
+  __TEXT.__auth_stubs: 0x10d0
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x2a78
-  __TEXT.__constg_swiftt: 0xb78
-  __TEXT.__swift5_typeref: 0xc52
+  __TEXT.__const: 0x2a98
+  __TEXT.__constg_swiftt: 0xb80
+  __TEXT.__swift5_typeref: 0xc5a
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x6a0
-  __TEXT.__swift5_fieldmd: 0x85c
+  __TEXT.__swift5_reflstr: 0x6b0
+  __TEXT.__swift5_fieldmd: 0x868
   __TEXT.__swift5_proto: 0x234
   __TEXT.__swift5_types: 0xb8
-  __TEXT.__cstring: 0x90e
+  __TEXT.__cstring: 0x8de
   __TEXT.__swift5_mpenum: 0x24
   __TEXT.__swift5_assocty: 0xa0
   __TEXT.__swift_as_entry: 0x90
   __TEXT.__swift_as_ret: 0x98
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_capture: 0x190
-  __TEXT.__oslogstring: 0x98a
+  __TEXT.__swift5_capture: 0x18c
+  __TEXT.__oslogstring: 0xafa
   __TEXT.__swift5_types2: 0x10
-  __TEXT.__unwind_info: 0xcd0
-  __TEXT.__eh_frame: 0x1cc8
+  __TEXT.__unwind_info: 0xcc0
+  __TEXT.__eh_frame: 0x1c20
   __TEXT.__objc_classname: 0x1e3
-  __TEXT.__objc_methname: 0x249
+  __TEXT.__objc_methname: 0x279
   __TEXT.__objc_methtype: 0xb4
   __TEXT.__objc_stubs: 0x40
   __DATA_CONST.__got: 0x1c8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb0
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__auth_got: 0x870
   __AUTH_CONST.__const: 0x16f0
-  __AUTH_CONST.__objc_const: 0x6e8
+  __AUTH_CONST.__objc_const: 0x708
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x780
-  __DATA.__data: 0xba8
+  __AUTH.__data: 0x788
+  __DATA.__data: 0xbb8
   __DATA.__bss: 0x4600
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 39C1D1F8-F9B8-31B6-A358-C23411976F35
-  Functions: 959
-  Symbols:   550
-  CStrings:  155
+  UUID: F1496E20-B38F-3E3E-92D3-C430CC1C740B
+  Functions: 957
+  Symbols:   551
+  CStrings:  159
 
Symbols:
+ _associated conformance 26ManagedBackgroundAssetsXPC10ConnectionC19TaskLocalContextKey33_7B6424F3C6A0485093FCC858E779505FLLOSHAASQ
+ _get_type_metadata 15Synchronization5MutexVy26ManagedBackgroundAssetsXPC14XPCActorSystemC6Actors33_3387A5A66F1C7ED96386BC11DC3A0326LLVG noncopyable.23
+ _get_type_metadata 15Synchronization5MutexVys5Error_pSgG noncopyable.22
+ _objectdestroy.67Tm
+ _symbolic _____ 26ManagedBackgroundAssetsXPC10ConnectionC19TaskLocalContextKey33_7B6424F3C6A0485093FCC858E779505FLLO
+ _symbolic _______________y__________GIeghg_IeghHgng_ 26ManagedBackgroundAssetsXPC17AddressedEnvelopeC AA11MessageInfoV s6ResultOsRi_zRi0_zrlE 10Foundation4DataV AA18XPCInvocationErrorV
+ _symbolic _____y______pSgG 15Synchronization5MutexVAARi_zrlE s5ErrorP
+ _symbolic y___________y_____y__________GYbctYaYbc 26ManagedBackgroundAssetsXPC17AddressedEnvelopeC AA11MessageInfoV s6ResultOsRi_zRi0_zrlE 10Foundation4DataV AA18XPCInvocationErrorV
- _associated conformance 26ManagedBackgroundAssetsXPC10ConnectionC11PeerHandler33_7B6424F3C6A0485093FCC858E779505FLLV19TaskLocalContextKeyOSHAASQ
- _get_type_metadata 15Synchronization5MutexVy26ManagedBackgroundAssetsXPC14XPCActorSystemC6Actors33_3387A5A66F1C7ED96386BC11DC3A0326LLVG noncopyable.22
- _objc_release_x21
- _objectdestroy.66Tm
- _symbolic _____ 26ManagedBackgroundAssetsXPC10ConnectionC11PeerHandler33_7B6424F3C6A0485093FCC858E779505FLLV19TaskLocalContextKeyO
- _symbolic _______________y__________G______pIeghgzo_AG_pIeghHgngzo_ 26ManagedBackgroundAssetsXPC17AddressedEnvelopeC AA11MessageInfoV s6ResultOsRi_zRi0_zrlE 10Foundation4DataV AA18XPCInvocationErrorV s0M0P
- _symbolic y___________y_____y__________GYbKctYaYbKc 26ManagedBackgroundAssetsXPC17AddressedEnvelopeC AA11MessageInfoV s6ResultOsRi_zRi0_zrlE 10Foundation4DataV AA18XPCInvocationErrorV
CStrings:
+ " initialization error: "
+ "A manual, asynchronous message couldn’t be handled due to an initialization failure: %{public}@"
+ "A manual, synchronous message couldn’t be handled due to an initialization failure: %{public}@"
+ "A message couldn’t be handled due to an initialization failure: %{public}@"
+ "The XPC distributed actor system has been deinitialized."
+ "initializationError"
- "There was an attempt to resign the ID “"
- "”, which doesn’t exist."

```
