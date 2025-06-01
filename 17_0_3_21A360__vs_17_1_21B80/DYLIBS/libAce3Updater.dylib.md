## libAce3Updater.dylib

> `/usr/lib/updaters/libAce3Updater.dylib`

```diff

-916.0.46.0.0
-  __TEXT.__text: 0x1705c
+916.40.22.0.2
+  __TEXT.__text: 0x175e8
   __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0x31c
-  __TEXT.__cstring: 0x37f4
+  __TEXT.__objc_methlist: 0x384
+  __TEXT.__cstring: 0x3a32
   __TEXT.__const: 0x128
-  __TEXT.__oslogstring: 0x1c
-  __TEXT.__unwind_info: 0x5dc
-  __TEXT.__objc_classname: 0x83
-  __TEXT.__objc_methname: 0x8d6
-  __TEXT.__objc_methtype: 0x6ba
-  __TEXT.__objc_stubs: 0x860
+  __TEXT.__oslogstring: 0x7
+  __TEXT.__unwind_info: 0x604
+  __TEXT.__objc_classname: 0x84
+  __TEXT.__objc_methname: 0x9f9
+  __TEXT.__objc_methtype: 0x6d2
+  __TEXT.__objc_stubs: 0x960
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x3e8
+  __DATA_CONST.__const: 0x410
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x690
-  __DATA_CONST.__objc_selrefs: 0x258
-  __AUTH_CONST.__cfstring: 0xbe0
+  __DATA_CONST.__objc_const: 0x770
+  __DATA_CONST.__objc_selrefs: 0x298
+  __AUTH_CONST.__cfstring: 0xde0
   __AUTH_CONST.__objc_const: 0x1a8
   __AUTH_CONST.__auth_got: 0x408
   __AUTH.__objc_data: 0x190
   __DATA.__objc_classrefs: 0x50
   __DATA.__objc_superrefs: 0x18
-  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x27
   __DATA.__bss: 0xb64
   __DATA.__common: 0x1

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA30C554-43A5-35CC-BE65-ADE2DB3C21C8
-  Functions: 767
-  Symbols:   1358
-  CStrings:  686
+  UUID: 072274DB-6A53-3B7B-B9B3-55EAC4D5BAB3
+  Functions: 776
+  Symbols:   1388
+  CStrings:  745
 
Symbols:
+ -[Ace3UpdaterInstance namePrefix]
+ -[UARPSoCUpdaterInstance namePrefix]
+ -[UARPSoCUpdaterInstance name]
+ -[UARPSoCUpdaterInstance printUpdaterMode]
+ -[UARPSoCUpdaterInstance skipSameVersion]
+ -[UARPSoCUpdaterInstance stagingCompleteWithStatus:reason:]
+ -[UARPSoCUpdaterInstance updateStagingProgressWithBytesSent:bytesTotal:]
+ -[UARPSoCUpdaterInstance updaterMode]
+ _OBJC_IVAR_$_UARPSoCUpdaterInstance._lastPercentComplete
+ _OBJC_IVAR_$_UARPSoCUpdaterInstance._name
+ _OBJC_IVAR_$_UARPSoCUpdaterInstance._nextUpdateProgressReportPercentThreshold
+ _OBJC_IVAR_$_UARPSoCUpdaterInstance._skipSameVersion
+ _OBJC_IVAR_$_UARPSoCUpdaterInstance._stagingResult
+ _OBJC_IVAR_$_UARPSoCUpdaterInstance._updaterMode
+ _SoCUpdaterGetMode
+ _StringForSoCUpdaterMode
+ _objc_msgSend$isEqual:
+ _objc_msgSend$name
+ _objc_msgSend$namePrefix
+ _objc_msgSend$printUpdaterMode
+ _objc_msgSend$skipSameVersion
+ _objc_msgSend$stagingCompleteWithStatus:reason:
+ _objc_msgSend$updateStagingProgressWithBytesSent:bytesTotal:
+ _objc_msgSend$updaterMode
- _UARPSoCUpdaterStagingProgress.cold.1
CStrings:
+ "\x01\x134!1"
+ "%@ Staging Complete"
+ "%@ Update: %u%%"
+ "%@ Update: 100%%"
+ "%@: Continuing after TSS offer."
+ "%@: Continuing after staging."
+ "%@: Detected updater mode %s"
+ "%@: Firmware staging failed. Status: 0x%08x (%s), Reason: 0x%08x (%s)"
+ "%@: TSS request signal waiting callbacks"
+ "%@: Waiting for TSS offer to complete..."
+ "%@: Waiting for staging to complete..."
+ "%@: staging complete signaling waiting callbacks"
+ "%s: %@ Offering Firmware"
+ "%s[%u]"
+ "Ace3 skip same version: %s"
+ "BootedOS"
+ "Expected more data: actual_more_data=0x%X, length=0x%X, (current_index + bytes_to_write) = 0x%X\n"
+ "Limited"
+ "No"
+ "OTA Preflight"
+ "OTA Stage 1"
+ "OTA Stage 2"
+ "PreflightContext"
+ "Q"
+ "Q16@0:8"
+ "TB,R,V_skipSameVersion"
+ "TQ,R,V_updaterMode"
+ "Tethered"
+ "Unknown"
+ "Unrecognized"
+ "Yes"
+ "_lastPercentComplete"
+ "_name"
+ "_nextUpdateProgressReportPercentThreshold"
+ "_stagingResult"
+ "_updaterMode"
+ "ace3"
+ "isEqual:"
+ "name"
+ "namePrefix"
+ "printUpdaterMode"
+ "skipSameVersion"
+ "stagingCompleteWithStatus:reason:"
+ "uarp"
+ "updateStagingProgressWithBytesSent:bytesTotal:"
+ "updaterMode"
+ "v24@0:8I16I20"
- "\x01\x134A"
- "%s: Offering Firmware"
- "%s: Progress (%d/%d)"
- "void UARPSoCUpdaterStagingProgress(void *, uint32_t, uint32_t)"

```
