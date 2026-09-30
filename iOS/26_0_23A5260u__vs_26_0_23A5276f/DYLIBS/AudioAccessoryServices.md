## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`

```diff

-30.45.3.0.0
-  __TEXT.__text: 0x3d270
+30.48.2.1.2
+  __TEXT.__text: 0x3e8a0
   __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x4e0c
+  __TEXT.__objc_methlist: 0x4e6c
   __TEXT.__const: 0x290
-  __TEXT.__gcc_except_tab: 0xec4
-  __TEXT.__cstring: 0xb546
-  __TEXT.__unwind_info: 0x1000
-  __TEXT.__objc_classname: 0x620
-  __TEXT.__objc_methname: 0xab17
-  __TEXT.__objc_methtype: 0x133c
-  __TEXT.__objc_stubs: 0x5860
+  __TEXT.__gcc_except_tab: 0xef0
+  __TEXT.__cstring: 0xb9fe
+  __TEXT.__unwind_info: 0x1030
+  __TEXT.__objc_classname: 0x62e
+  __TEXT.__objc_methname: 0xacd4
+  __TEXT.__objc_methtype: 0x137f
+  __TEXT.__objc_stubs: 0x5a00
   __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0xe80
-  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__const: 0xed8
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22e0
+  __DATA_CONST.__objc_selrefs: 0x2348
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x448
-  __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x2100
-  __AUTH_CONST.__objc_const: 0x8f48
+  __AUTH_CONST.__const: 0x1c0
+  __AUTH_CONST.__cfstring: 0x2220
+  __AUTH_CONST.__objc_const: 0x9008
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x780
+  __AUTH.__objc_data: 0x7d0
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x880
-  __DATA.__data: 0xbf8
+  __DATA.__objc_ivar: 0x884
+  __DATA.__data: 0xc68
   __DATA.__common: 0x8
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x6e0

   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8F7CCEAE-AA98-3863-BD25-637C277DA3F5
-  Functions: 2091
-  Symbols:   6340
-  CStrings:  3917
+  UUID: 9C2ED440-9844-3F06-B54C-D58CDF27E128
+  Functions: 2109
+  Symbols:   6394
+  CStrings:  3983
 
Symbols:
+ +[AAAssetHelper _bluetoothProductDefaultAsset:]
+ +[AAAssetHelper _bluetoothProductIDToAsset:]
+ +[AAAssetHelper _bluetoothProductIDToAsset:].cold.1
+ +[AAAssetHelper _bluetoothProductIDToAsset:].cold.2
+ +[AAAssetHelper _bluetoothProductIDToAsset:withColor:]
+ +[AAAssetHelper _bluetoothProductIDToAsset:withColor:].cold.1
+ +[AAAssetHelper _bluetoothProductIDToAsset:withColor:].cold.2
+ +[AAAssetHelper _bluetoothProductIDToCaseAsset:withColor:]
+ +[AAAssetHelper _bluetoothProductIDToCaseAsset:withColor:].cold.1
+ +[AAAssetHelper _bluetoothProductIDToCaseAsset:withColor:].cold.2
+ +[AAAssetHelper _productCaseHasColors:]
+ +[AAAssetHelper _productColorAssetExists:withColor:]
+ +[AAAssetHelper _productHasColors:]
+ +[AAAssetHelper bluetoothProductIDToAsset:withColor:isCase:]
+ -[AADeviceBatteryInfo _updateCombinedBatteryWithChanges:]
+ -[AADeviceBatteryInfo _updateCombinedBatteryWithChanges:].cold.1
+ -[AADeviceBatteryInfo applyOverrideFromStr:forBatteryType:]
+ -[AADeviceBatteryInfo applyOverrideFromStr:forBatteryType:].cold.1
+ -[AADeviceBatteryInfo applyOverrideFromStr:forBatteryType:].cold.2
+ -[AADeviceBatteryInfo applyOverrideFromStr:forBatteryType:].cold.3
+ -[AADeviceBatteryInfo clearExpiredBatteries].cold.1
+ -[AADeviceBatteryInfo updateWithLostAANearbyDevice:]
+ -[AADeviceManager deviceManagerFoundDevice:].cold.2
+ -[AAProxCardsInfo fitEducationNotificationsShownCount]
+ -[AAProxCardsInfo setFitEducationNotificationsShownCount:]
+ _AABatteryTypeToString
+ _OBJC_CLASS_$_AAAssetHelper
+ _OBJC_IVAR_$_AAProxCardsInfo._fitEducationNotificationsShownCount
+ _OBJC_METACLASS_$_AAAssetHelper
+ __OBJC_$_CLASS_METHODS_AAAssetHelper
+ __OBJC_CLASS_RO_$_AAAssetHelper
+ __OBJC_METACLASS_RO_$_AAAssetHelper
+ _gLogCategory_AAAssetHelper
+ _objc_msgSend$_bluetoothProductDefaultAsset:
+ _objc_msgSend$_bluetoothProductIDToAsset:
+ _objc_msgSend$_bluetoothProductIDToAsset:withColor:
+ _objc_msgSend$_bluetoothProductIDToCaseAsset:withColor:
+ _objc_msgSend$_productCaseHasColors:
+ _objc_msgSend$_productColorAssetExists:withColor:
+ _objc_msgSend$_productHasColors:
+ _objc_msgSend$_updateCombinedBatteryWithChanges:
+ _objc_msgSend$containsString:
+ _objc_msgSend$doubleValueSafe
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$setHeadGestureProxCardShown:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$substringFromIndex:
- -[AADeviceBatteryInfo _updateCombinedBattery]
- -[AASensorService subscribeWithFlags:]
- -[AASensorService subscribeWithFlags:rate:]
- -[AASensorService subscribeWithFlagsWithCompletion:completion:]
- -[AASensorService subscribeWithFlagsWithCompletion:rate:completion:]
- -[AASensorService unsubscribeWithFlags:]
- GCC_except_table22
- GCC_except_table29
- ___38-[AASensorService subscribeWithFlags:]_block_invoke
- ___43-[AASensorService subscribeWithFlags:rate:]_block_invoke
- ___block_literal_global.67
- ___block_literal_global.71
- _objc_msgSend$_updateCombinedBattery
- _objc_msgSend$cloudRecordInfoLoaded
CStrings:
+ "%s Battery overwrite via prefs: %@"
+ "%s Battery overwrite: %@"
+ "+[AAAssetHelper _bluetoothProductIDToAsset:]"
+ "+[AAAssetHelper _bluetoothProductIDToAsset:withColor:]"
+ "+[AAAssetHelper _bluetoothProductIDToCaseAsset:withColor:]"
+ "+[AAAssetHelper bluetoothProductIDToAsset:withColor:isCase:]"
+ ",\n%@"
+ ", comb LR %@"
+ "-%u"
+ "-[AADeviceBatteryInfo _updateCombinedBatteryWithChanges:]"
+ "-[AADeviceBatteryInfo applyOverrideFromStr:forBatteryType:]"
+ "-[AADeviceBatteryInfo clearExpiredBatteries]"
+ "-[AADeviceManager discoveredDevices]"
+ "-default"
+ "@20@0:8I16"
+ "@24@0:8I16C20"
+ "@28@0:8I16C20B24"
+ "AAAssetHelper"
+ "AADevice id: %@, "
+ "Asset for PID: %u does not exist for color %u, using default colored asset"
+ "Asset for PID: %u exist in color %u"
+ "Asset found for PID: %u with color code: %lu. Asset name: %@ "
+ "AutoANC: "
+ "B20@0:8I16"
+ "B24@0:8I16C20"
+ "B32@0:8@16q24"
+ "Banner-PID-%u"
+ "Banner-PID-%u-%u-Case"
+ "Banner-PID-%u-Case"
+ "Banner-PID-%u-default-Case"
+ "Battery expired, removing: %@"
+ "Bbl: "
+ "Calling device found handler for client ID 0x%X"
+ "Cam ctl: "
+ "Case Asset for PID: %u does not exist for color %u, using default color"
+ "Case Asset for PID: %u exist in color %u"
+ "Case for PID: %u does not have colors, using default asset"
+ "Chr rem: "
+ "Cleared delayed notification for lost sensor data availability"
+ "Color is custom, using default asset for PID."
+ "Color is custom, using default case asset for  PID."
+ "Combining battery with different charging states, using highest. L: %u, R: %u -> %u"
+ "Finding Asset for PID: %u with color code: %u"
+ "Finding Case Asset for PID: %u with color code: %u"
+ "HA: "
+ "HG: "
+ "HP: "
+ "HR: "
+ "HT: "
+ "Invalid %s Battery overwrite: %@"
+ "Lsn: "
+ "Misc Info: "
+ "Notify about sensor data availability change, flags: %d, force %s"
+ "OBC"
+ "OBC: "
+ "Pl: "
+ "Product with PID: %u does not come in colors, using default asset"
+ "SS: "
+ "Sending %@"
+ "Sending %d discovered device to client ID 0x%X"
+ "Sldt: "
+ "SrMt: "
+ "TQ,V_fitEducationNotificationsShownCount"
+ "Triggered %.1fs delayed notification for lost sensor data availability"
+ "Using PID: %u instead of %u"
+ "_bluetoothProductDefaultAsset:"
+ "_bluetoothProductIDToAsset:"
+ "_bluetoothProductIDToAsset:withColor:"
+ "_bluetoothProductIDToCaseAsset:withColor:"
+ "_fitEducationNotificationsShownCount"
+ "_productCaseHasColors:"
+ "_productColorAssetExists:withColor:"
+ "_productHasColors:"
+ "_updateCombinedBatteryWithChanges:"
+ "acct %s, "
+ "ag enr '%@', "
+ "aos %s, "
+ "applyOverrideFromStr:forBatteryType:"
+ "as %s, "
+ "bluetoothProductIDToAsset:withColor:isCase:"
+ "cap %s, "
+ "cfg %@, "
+ "cfg %s, "
+ "containsString:"
+ "decl %s, "
+ "det %s, "
+ "doubleValueSafe"
+ "en %s, "
+ "enh trn %s,"
+ "enr %s, "
+ "fitEducationNotificationsShownCount"
+ "gs %s, "
+ "hasPrefix:"
+ "hide er %s, "
+ "lst conn '%@', "
+ "md %s, "
+ "missing"
+ "ml %@, "
+ "nm %@, "
+ "off %s, "
+ "pr %s, "
+ "sc %s, "
+ "setFitEducationNotificationsShownCount:"
+ "stringByAppendingFormat:"
+ "stringByAppendingString:"
+ "substringFromIndex:"
+ "temp mg %s, "
+ "tg %s, "
+ "tgl %s, "
+ "top lvl %s, "
+ "updateWithLostAANearbyDevice:"
- ", Md '%@'"
- ", combined lt rt %@"
- "AG EnrolledTime '%@', "
- "AStS %s, "
- "AudioAccessoryDevice identifier: %@, "
- "Cleared delayed notifcation for lost sensor data availability"
- "HRM En %s, "
- "HT Cap %s, "
- "LsMC %@, "
- "LsMd Off %s, "
- "LsnM %s, "
- "Lst Conn '%@', "
- "Md %@, "
- "Misc info: "
- "Nm %@, "
- "Notify about sensor data availablibity change, flags: %d, force %s"
- "OBC Cap %s, "
- "OBC En %s, "
- "Triggered %.1fs delayed notifcation for lost sensor data availability"
- "_updateCombinedBattery"
- "acceptReplyPlayPause Cfg %s, "
- "autoANC Cap %s, "
- "autoANC strength %s, "
- "bbl Cap %s, "
- "bbl Cfg %s, "
- "cam ctl Cap %s, "
- "cam ctl Cfg %s, "
- "chr rem Cap %s, "
- "chr rem En %s, "
- "declineDismissSkip Cfg %s, "
- "detected hgs %s, "
- "enh trn Ver %s,"
- "ha Cap %s, "
- "ha En %s, "
- "ha Enr %s, "
- "ha top lvl %s, "
- "haGS En %s, "
- "hg tgl %s, "
- "hide er dt %s, "
- "hp Cap %s, "
- "plmd %s, "
- "prpl %s, "
- "scpl %s, "
- "sldt Cap %s, "
- "sldt Tg %s, "
- "srMt Cap %s, "
- "srMt Tg %s, "
- "stAoS %s, "
- "subscribeWithFlags:"
- "subscribeWithFlags:rate:"
- "subscribeWithFlagsWithCompletion:completion:"
- "subscribeWithFlagsWithCompletion:rate:completion:"
- "temp mg paired %s, "
- "unsubscribeWithFlags:"
- "v24@0:8I16I20"

```
