## CoreTime

> `/System/Library/PrivateFrameworks/CoreTime.framework/Versions/A/CoreTime`

```diff

-334.0.2.0.0
-  __TEXT.__text: 0x6ad4
+334.0.4.1.0
+  __TEXT.__text: 0x681c
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x23c
-  __TEXT.__const: 0xf0
+  __TEXT.__objc_methlist: 0x28c
+  __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x6c
   __TEXT.__cstring: 0xdda
   __TEXT.__oslogstring: 0x4ae
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0x210
+  __TEXT.__unwind_info: 0x238
   __TEXT.__objc_classname: 0x5a
   __TEXT.__objc_methname: 0x5d2
   __TEXT.__objc_methtype: 0x103

   __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0x2f0
   __AUTH_CONST.__cfstring: 0xde0
-  __AUTH_CONST.__objc_const: 0x440
+  __AUTH_CONST.__objc_const: 0x3c8
   __AUTH_CONST.__objc_intobj: 0x4e0
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1F67E67-A2B5-312E-A4A3-6A17F34217DF
-  Functions: 155
-  Symbols:   486
+  UUID: AEA3AD51-9D8D-3AA2-99B9-CDEEBE2CC513
+  Functions: 187
+  Symbols:   546
   CStrings:  421
 
Symbols:
+ +[TMTime timeWithUtc_s:utcUnc_s:rtc_s:sf:source:].cold.1
+ +[TMTime timeWithUtc_s:utcUnc_s:rtc_s:sf:source:].cold.2
+ +[TMTime timeWithUtc_s:utcUnc_s:rtc_s:sf:source:].cold.3
+ +[TMTime timeWithUtc_s:utcUnc_s:rtc_s:sf:source:].cold.4
+ -[TMTime(ConvenienceConversions) setRtc_s:].cold.1
+ -[TMTime(ConvenienceConversions) setRtc_s:].cold.2
+ -[TMTime(ConvenienceConversions) setUtc_s:].cold.1
+ -[TMTime(ConvenienceConversions) setUtc_s:].cold.2
+ TMCmdFromName.cold.1
+ TMConfirmTimeZone.cold.1
+ TMDeviceHasPMU.cold.1
+ TMFetchNTP.cold.1
+ TMGetKernelMonotonicClockResolution.cold.1
+ TMProvideBBTime.cold.1
+ TMProvideBBTime.cold.2
+ TMProvideBBTime.cold.3
+ TMProvideBBTime.cold.4
+ TMProvideCellularTimeZone.cold.1
+ TMProvideCellularTimeZone.cold.2
+ TMProvideCellularTimeZone.cold.3
+ TMSetAuthenticatedSourceTime.cold.1
+ TMSetAuthenticatedSourceTime.cold.2
+ TMSetAuthenticatedSourceTime.cold.3
+ TMSetAuthenticatedSourceTime.cold.4
+ TMSetAuthenticatedSourceTime.cold.5
+ TMSetAutomaticTimeEnabled.cold.1
+ TMSetAutomaticTimeZoneEnabled.cold.1
+ TMSetManualTime.cold.1
+ TMSetManualTime.cold.2
+ TMSetManualTime.cold.3
+ TMSetSourceAvailable.cold.1
+ TMSetSourceTime.cold.1
+ TMSetSourceTime.cold.2
+ TMSetSourceTime.cold.3
+ TMSetSourceTime.cold.4
+ TMSetSourceTime.cold.5
+ TMSetSourceTime.cold.6
+ TMSetSourceTime.cold.7
+ TMSetSourceTimeZone.cold.1
+ TMSetSourceUnavailable.cold.1
+ TMSetTestSourceTime.cold.1
+ TMSetTestSourceTime.cold.2
+ TMSetTestSourceTime.cold.3
+ TMSetTestSourceTime.cold.4
+ TMSetTestSourceTime.cold.5
+ TMSetTestSourceTime.cold.6
+ TMSetTestSourceTime.cold.7
+ TMSrcFromName.cold.1
+ _TMConnectionQueue.cold.1
+ _TMCopyConnection.cold.1
+ _TMGetKernelMonotonicClock.cold.3
+ _TMGetKernelMonotonicClock.cold.4
+ _TMKernelMonotonicClockOffset.cold.4
+ _TMKernelMonotonicClockOffset.cold.5
+ _TMSyncKernelMonotonicClock.cold.2
+ _TMSyncKernelMonotonicClock.cold.3
+ ___TMCopyConnection_block_invoke.cold.1
+ ___TMSyncKernelMonotonicClock_block_invoke.cold.2
- _OUTLINED_FUNCTION_2

```
