## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-  __TEXT.__text: 0x6ecb4
+  __TEXT.__text: 0x6f0a0
   __TEXT.__const: 0x3df9
-  __TEXT.__gcc_except_tab: 0x58e8
-  __TEXT.__cstring: 0x2d99
-  __TEXT.__oslogstring: 0x9c6f
-  __TEXT.__unwind_info: 0x23e8
+  __TEXT.__gcc_except_tab: 0x5918
+  __TEXT.__cstring: 0x2dab
+  __TEXT.__oslogstring: 0x9ccc
+  __TEXT.__unwind_info: 0x23f8
   __TEXT.__auth_stubs: 0x13f0
   __DATA_CONST.__const: 0xdf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x250
-  __AUTH_CONST.__const: 0x49d0
-  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__const: 0x49e0
+  __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x9e8
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1786
-  Symbols:   3267
-  CStrings:  1510
+  Functions: 1788
+  Symbols:   3270
+  CStrings:  1514
 
Sections:
~ __DATA_CONST.__const : content changed
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
+ "ImsRegistrationState: UE is Registered for %s (0x%08x) on %{public}s%s (%s)"
+ "ManagedConnection"
+ "getRCSManagedConnection %{bool}d"
+ "getRCSManagedConnection: Null PersonalityShop"
- "ImsEstablishmentTimer: Starting RCS Establishment timer: %u seconds"
- "ImsRegistrationState: UE is Registered for %s on %{public}s%s (%s)"

```
