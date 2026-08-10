## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`

```diff

-13482.1.0.0.0
-  __TEXT.__text: 0x6faa0
-  __TEXT.__const: 0x3ef9
-  __TEXT.__gcc_except_tab: 0x5988
-  __TEXT.__cstring: 0x36c4
-  __TEXT.__oslogstring: 0x9e3c
-  __TEXT.__unwind_info: 0x2420
+13487.3.0.0.0
+  __TEXT.__text: 0x707d4
+  __TEXT.__const: 0x3f09
+  __TEXT.__gcc_except_tab: 0x5a38
+  __TEXT.__cstring: 0x36e0
+  __TEXT.__oslogstring: 0xa272
+  __TEXT.__unwind_info: 0x2458
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xdf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x4a60
+  __AUTH_CONST.__const: 0x4a90
   __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1798
-  Symbols:   2959
-  CStrings:  1458
+  Functions: 1804
+  Symbols:   2973
+  CStrings:  1475
 
Symbols:
+ GCC_except_table119
+ GCC_except_table160
+ GCC_except_table176
+ GCC_except_table189
+ GCC_except_table194
+ GCC_except_table201
+ GCC_except_table204
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table218
+ GCC_except_table229
+ GCC_except_table230
+ GCC_except_table235
+ GCC_except_table241
+ GCC_except_table246
+ GCC_except_table258
+ GCC_except_table259
+ GCC_except_table264
+ GCC_except_table265
+ GCC_except_table270
+ GCC_except_table279
+ GCC_except_table282
+ GCC_except_table283
+ GCC_except_table286
+ GCC_except_table287
+ GCC_except_table295
+ GCC_except_table296
+ GCC_except_table349
+ GCC_except_table355
+ GCC_except_table358
+ GCC_except_table366
+ GCC_except_table373
+ GCC_except_table378
+ GCC_except_table381
+ GCC_except_table384
+ GCC_except_table392
+ GCC_except_table396
+ GCC_except_table401
+ GCC_except_table405
+ GCC_except_table413
+ GCC_except_table419
+ GCC_except_table428
+ GCC_except_table431
+ GCC_except_table441
+ GCC_except_table447
+ GCC_except_table450
+ GCC_except_table461
+ GCC_except_table464
+ GCC_except_table467
+ GCC_except_table474
+ GCC_except_table477
+ GCC_except_table482
+ GCC_except_table483
+ GCC_except_table488
+ GCC_except_table491
+ GCC_except_table497
+ GCC_except_table501
+ GCC_except_table511
+ GCC_except_table514
+ GCC_except_table519
+ GCC_except_table522
+ GCC_except_table95
+ _CFAbsoluteTimeGetCurrent
+ _CFDateCreate
+ __Z8asString18RegistrationStatus
+ __ZN26SystemDeterminationManager23handleExitLowPower_syncEv
+ __ZN2sd23RCSSubscriberController14checkRegTimersEv
+ __ZN2sd23RCSSubscriberController21handleSystemWake_syncEv
+ __ZN2sd27IMSSubscriberControllerBase21handleSystemWake_syncEv
+ __ZN3ctu9SharedRefIK8__CFDateNS_2cf16cfretain_functorENS3_17cfrelease_functorES2_ED2Ev
+ __ZTI23PowerAssertionInterface
+ __ZThn48_N26SystemDeterminationManager23handleExitLowPower_syncEv
+ _time
- GCC_except_table104
- GCC_except_table174
- GCC_except_table175
- GCC_except_table188
- GCC_except_table191
- GCC_except_table196
- GCC_except_table205
- GCC_except_table213
- GCC_except_table216
- GCC_except_table222
- GCC_except_table233
- GCC_except_table237
- GCC_except_table238
- GCC_except_table243
- GCC_except_table255
- GCC_except_table257
- GCC_except_table261
- GCC_except_table262
- GCC_except_table267
- GCC_except_table277
- GCC_except_table280
- GCC_except_table281
- GCC_except_table284
- GCC_except_table285
- GCC_except_table291
- GCC_except_table292
- GCC_except_table346
- GCC_except_table348
- GCC_except_table356
- GCC_except_table364
- GCC_except_table371
- GCC_except_table374
- GCC_except_table379
- GCC_except_table380
- GCC_except_table390
- GCC_except_table394
- GCC_except_table397
- GCC_except_table403
- GCC_except_table411
- GCC_except_table417
- GCC_except_table424
- GCC_except_table429
- GCC_except_table439
- GCC_except_table445
- GCC_except_table448
- GCC_except_table459
- GCC_except_table462
- GCC_except_table463
- GCC_except_table468
- GCC_except_table475
- GCC_except_table478
- GCC_except_table481
- GCC_except_table486
- GCC_except_table489
- GCC_except_table493
- GCC_except_table499
- GCC_except_table507
- GCC_except_table512
- GCC_except_table517
- GCC_except_table520
CStrings:
+ "5wi.ctr:: \t fExpirationTime = %ld, fRefreshTime = %ld (now = %ld)"
+ "5wi.ctr:: \t pushPayload = %{bool}d"
+ "Clearing pushPayload (proceedInitializeRcsClient)"
+ "Clearing pushPayload (proceedTransientInitialize)"
+ "IMSRegistrationActive: fExpirationTime=%ld, fRefreshTime=%ld (now=%ld)"
+ "PCSCF connected but no longer qualified to register - aborting"
+ "PCSCF connection ready for re-registration (TransientDisconnected)"
+ "RCSRegRefresh: Scheduled CPPower wake in %u seconds"
+ "Skipping fLastRegisteredNetworkInfo update: no valid cell info (RAT=%s DataMode=%s regStatus=%s)"
+ "abortRCSRegRefreshTimer: cleared fExpirationTime=%ld, fRefreshTime=%ld"
+ "checkRegTimers: not yet due, rescheduling with %u seconds remaining"
+ "checkRegTimers: now=%ld, fRefreshTime=%ld, fExpirationTime=%ld"
+ "checkRegTimers: refresh overdue by %lds, triggering now"
+ "checkRegTimers: registration expired during sleep (overdue by %lds), reconnecting"
+ "com.apple.sd.RCSRegRefresh."
+ "handleExitLowPower_sync: system woke, notifying %zu lazuli controllers"
+ "handleSystemWake_sync: system woke, checking reg timers"
+ "onRCSRegRefreshTimeout: in TD, trigger new PCSCF connection!"
+ "onRCSRegRefreshTimeout: not in TD, (still registered), directly initialize with existing connection!"
- "PCSCF connection ready for Push registration"
- "RCSRegRefreshTimer: already registered, re-arming timer."
```
