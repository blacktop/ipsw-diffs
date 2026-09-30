## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-  __TEXT.__text: 0x6f278
+  __TEXT.__text: 0x6f654
   __TEXT.__const: 0x3ef9
-  __TEXT.__gcc_except_tab: 0x5944
-  __TEXT.__cstring: 0x3691
-  __TEXT.__oslogstring: 0x9ced
-  __TEXT.__unwind_info: 0x2408
+  __TEXT.__gcc_except_tab: 0x597c
+  __TEXT.__cstring: 0x36a3
+  __TEXT.__oslogstring: 0x9d41
+  __TEXT.__unwind_info: 0x2418
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xdf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x4a50
-  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__const: 0x4a60
+  __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1796
-  Symbols:   4203
-  CStrings:  1523
+  Functions: 1798
+  Symbols:   4206
+  CStrings:  1527
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
Symbols:
+ GCC_except_table173
+ __ZN2sd23RCSSubscriberController26startImsEstablishmentTimerEj
+ __ZNK2sd18IMSSubscriberModel25isLazuliManagedConnectionEv
+ __ZNK2sd19IMSSubscriberConfig31getRCSManagedConnectionOverrideEv
+ __ZNK2sd27IMSSubscriberControllerBase19isManagedConnectionEv
+ __ZThn48_NK2sd27IMSSubscriberControllerBase19isManagedConnectionEv
- GCC_except_table105
- GCC_except_table167
- GCC_except_table169
- GCC_except_table88
- GCC_except_table95
- __ZN2sd23RCSSubscriberController26startImsEstablishmentTimerEv
- __ZNK2sd27IMSSubscriberControllerBase20isLazuliCarrierBasedEv
- __ZThn48_NK2sd27IMSSubscriberControllerBase20isLazuliCarrierBasedEv
CStrings:
+ "ImsEstablishmentTimer: Starting RCS Establishment timer: %u + %u seconds"
+ "ManagedConnection"
+ "getRCSManagedConnection %{bool}d"
+ "getRCSManagedConnection: Null PersonalityShop"
- "ImsEstablishmentTimer: Starting RCS Establishment timer: %u seconds"

```
