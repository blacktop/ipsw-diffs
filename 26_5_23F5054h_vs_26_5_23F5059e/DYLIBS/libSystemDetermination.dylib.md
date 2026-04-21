## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-13185.1.0.0.0
-  __TEXT.__text: 0x604b4
-  __TEXT.__auth_stubs: 0x1190
+13186.1.0.0.0
+  __TEXT.__text: 0x600b8
+  __TEXT.__auth_stubs: 0x1180
   __TEXT.__const: 0x32b4
-  __TEXT.__gcc_except_tab: 0x50a8
+  __TEXT.__gcc_except_tab: 0x508c
   __TEXT.__cstring: 0x2c00
-  __TEXT.__oslogstring: 0x8ebc
-  __TEXT.__unwind_info: 0x1ea8
+  __TEXT.__oslogstring: 0x8c71
+  __TEXT.__unwind_info: 0x1eb0
   __DATA_CONST.__got: 0x268
   __DATA_CONST.__const: 0xdc0
-  __AUTH_CONST.__auth_got: 0x8d0
-  __AUTH_CONST.__const: 0x35f8
+  __AUTH_CONST.__auth_got: 0x8c8
+  __AUTH_CONST.__const: 0x3608
   __AUTH_CONST.__cfstring: 0x840
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x60

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: A89976FA-B81A-37DD-883C-CC2DABB7F746
-  Functions: 1418
-  Symbols:   3395
-  CStrings:  1388
+  UUID: 2B73D2BF-DD8A-3FBB-B630-1719F787BFB2
+  Functions: 1419
+  Symbols:   3394
+  CStrings:  1376
 
Symbols:
+ GCC_except_table137
+ GCC_except_table196
+ GCC_except_table199
+ GCC_except_table218
+ GCC_except_table219
+ GCC_except_table247
+ GCC_except_table285
+ GCC_except_table294
+ GCC_except_table303
+ GCC_except_table312
+ GCC_except_table321
+ GCC_except_table324
+ GCC_except_table330
+ GCC_except_table335
+ GCC_except_table394
+ GCC_except_table411
+ GCC_except_table87
+ __ZN2sd20imsServiceMaskToUintEN5caulk10option_setINS_14ImsServiceTypeEjEE
+ __ZN2sd23IMSSubscriberController13resetShutdownEv
- GCC_except_table109
- GCC_except_table156
- GCC_except_table216
- GCC_except_table217
- GCC_except_table235
- GCC_except_table245
- GCC_except_table266
- GCC_except_table275
- GCC_except_table284
- GCC_except_table293
- GCC_except_table302
- GCC_except_table311
- GCC_except_table320
- GCC_except_table323
- GCC_except_table329
- GCC_except_table331
- GCC_except_table333
- GCC_except_table393
- GCC_except_table397
- GCC_except_table406
- GCC_except_table77
- GCC_except_table95
- _TelephonyUtilIsOversteerEnabled
- __os_log_debug_impl
CStrings:
+ "#I 5wi.ctr:: \t fShutdownStarted = %{bool}d"
+ "#I IMS Registration Info: initializing for %s (0x%08x) over %{public}s%s (APN: %{public}s, hasLegacyRat=%d)"
+ "#I ImsEstablishmentTimer: Aborting IMS Establishment timer"
+ "#I ImsEstablishmentTimer: Aborting RCS Establishment timer"
+ "#I ImsEstablishmentTimer: Starting RCS Establishment timer: %u seconds"
+ "#I ImsRegistrationState: UE is Registered for %s (0x%08x) on %{public}s%s (%s)"
+ "#I LazuliInfoRemoved: Unwinding RCS stack: %s"
+ "#I New RCS registration started. Staring guard timer."
+ "#N ImsEstablishmentTimer: RCS Registration didn't succeed in %d seconds. Switch transport"
+ "#N LazuliControllerShutdown: erasing controller accountId=%s"
+ "IMSRegistrationEvent: RCS gave up registering - switching transport."
- "#D Async getting is LazuliThirdPartyApp"
- "#D Cellular footprint is not required for VoWiFi, ok to bring up IMS PDN"
- "#D Current DataContext is: %s. Checking CB key is not needed"
- "#D DCN already scheduled"
- "#D DomesticRoamingUpdate: roaming state %{bool}d"
- "#D EmergencyAccessNetworkInfoUpdate: Not in emergency call. Don't send emergency access network info update"
- "#D ISIM info didn't change"
- "#D ImsPdpActive: Lazuli mode. Country Of Origination not required"
- "#D ImsPdpActive: Not in iWLAN mode. Country Of Origination not required"
- "#D Not submitting RCSServiceDuration metric for zero duration"
- "#D Received PushURL: %{public}s"
- "#D Returning isCellularFootprintSeen as %{bool}d"
- "#D Roaming result remains as %s"
- "#D RoamingUpdate: Ignore undetermined roaming state %s"
- "#D Setting isCellularFootprintSeen to %{bool}d"
- "#D Stored PushURL: %{public}s"
- "#D Telephony was NOT %s successfully"
- "#D WiFiCalling-only mode: true. Baseband booted assertion required. iSimInfoReady: %{bool}d, deviceInfoReady: %{bool}d. BB booted assertion held: %{bool}d"
- "#D fInCallImsPref is inactive!"
- "#D handleCountryOfOrigination: mcc INT is: %u"
- "#I IMS Registration Info: initializing for %s over %{public}s%s (APN: %{public}s, hasLegacyRat=%d)"
- "#I ImsEstablishmentTimer: Aborting TIMS_Establishment timer"
- "#I ImsRegistrationState: UE is Registered for %s on %{public}s%s (%s)"

```
