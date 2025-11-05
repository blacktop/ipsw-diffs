## SetupAssistantSupport

> `/System/Library/PrivateFrameworks/SetupAssistantSupport.framework/Versions/A/SetupAssistantSupport`

```diff

-512.0.0.0.0
-  __TEXT.__text: 0xe3a4
+534.0.0.0.0
+  __TEXT.__text: 0xf76c
   __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x12e8
+  __TEXT.__objc_methlist: 0x1574
   __TEXT.__const: 0x94
-  __TEXT.__cstring: 0xab0
+  __TEXT.__cstring: 0xd3d
   __TEXT.__oslogstring: 0xaa4
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__unwind_info: 0x2d0
-  __TEXT.__objc_classname: 0x27b
-  __TEXT.__objc_methname: 0x3781
-  __TEXT.__objc_methtype: 0x6d1
-  __TEXT.__objc_stubs: 0x2460
+  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__objc_classname: 0x2bc
+  __TEXT.__objc_methname: 0x3966
+  __TEXT.__objc_methtype: 0x710
+  __TEXT.__objc_stubs: 0x27a0
   __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x218
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__const: 0x228
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xca8
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_selrefs: 0xdd0
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x200
   __AUTH_CONST.__const: 0x4b0
-  __AUTH_CONST.__cfstring: 0xe20
-  __AUTH_CONST.__objc_const: 0x2c00
+  __AUTH_CONST.__cfstring: 0x12e0
+  __AUTH_CONST.__objc_const: 0x2a88
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x190
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D79BE5EB-2744-313C-8B04-2EBED3A0E9CB
-  Functions: 451
-  Symbols:   1262
-  CStrings:  1050
+  UUID: 86C2AB7C-83FA-3DE8-9E0F-95AB526790A4
+  Functions: 464
+  Symbols:   1322
+  CStrings:  1154
 
Symbols:
+ +[SASExpressSettingsCreator createExpressSettingsUsingDictionary:]
+ +[SASLogging facility].cold.1
+ +[SASServerSupport sharedInstance].cold.1
+ -[SASProximityInformation fullName]
+ -[SASProximityInformation grammarInflection]
+ -[SASProximityInformation setFullName:]
+ -[SASProximityInformation setGrammarInflection:]
+ -[SASProximityInformationDictionaryCoder .cxx_destruct]
+ -[SASProximityInformationDictionaryCoder dataDictionary]
+ -[SASProximityInformationDictionaryCoder decodeBoolForKey:]
+ -[SASProximityInformationDictionaryCoder decodeObjectOfClasses:forKey:]
+ -[SASProximityInformationDictionaryCoder initWithDictionary:]
+ -[SASProximityInformationDictionaryCoder setDataDictionary:]
+ -[SASProximityInformationDictionaryCoder setGrammarInflectionGender:]
+ -[SASProximityInformationDictionaryCoder setWiFiPassword:]
+ -[SASProximityInformationDictionaryCoder setWiFiSSID:]
+ OBJC_IVAR_$_SASProximityInformation._fullName
+ OBJC_IVAR_$_SASProximityInformation._grammarInflection
+ OBJC_IVAR_$_SASProximityInformationDictionaryCoder._dataDictionary
+ _OBJC_CLASS_$_NSCoder
+ _OBJC_CLASS_$_SASExpressSettingsCreator
+ _OBJC_CLASS_$_SASProximityInformationDictionaryCoder
+ _OBJC_CLASS_$__NSAttributedStringGrammarInflection
+ _OBJC_METACLASS_$_NSCoder
+ _OBJC_METACLASS_$_SASExpressSettingsCreator
+ _OBJC_METACLASS_$_SASProximityInformationDictionaryCoder
+ __34-[SASProximitySession sendAction:]_block_invoke.22
+ __58-[SASCloudKitClient fetchRecords:inZone:group:completion:]_block_invoke.17
+ __OBJC_$_CLASS_METHODS_SASExpressSettingsCreator
+ __OBJC_$_INSTANCE_METHODS_SASProximityInformationDictionaryCoder
+ __OBJC_$_INSTANCE_VARIABLES_SASProximityInformationDictionaryCoder
+ __OBJC_$_PROP_LIST_SASProximityInformationDictionaryCoder
+ __OBJC_CLASS_RO_$_SASExpressSettingsCreator
+ __OBJC_CLASS_RO_$_SASProximityInformationDictionaryCoder
+ __OBJC_METACLASS_RO_$_SASExpressSettingsCreator
+ __OBJC_METACLASS_RO_$_SASProximityInformationDictionaryCoder
+ _kSASProximityInformationFullNameKey
+ _kSASProximityInformationGrammarInflectionKey
+ _objc_msgSend$CKItemErrorForID:
+ _objc_msgSend$dataDictionary
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$fullName
+ _objc_msgSend$grammarInflection
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$setAppearanceMode:
+ _objc_msgSend$setContentVersion:
+ _objc_msgSend$setDataDictionary:
+ _objc_msgSend$setDisplayZoomOption:
+ _objc_msgSend$setFileVaultEnabled:
+ _objc_msgSend$setFindMyOptIn:
+ _objc_msgSend$setFullName:
+ _objc_msgSend$setGender:
+ _objc_msgSend$setGrammarInflection:
+ _objc_msgSend$setScreenTimeEnabled:
+ _objc_msgSend$setSiriDataSharingOptIn:
+ _objc_msgSend$setSiriVoiceTriggerEnabled:
+ _objc_msgSend$setSoftwareUpdateAutoDownloadEnabled:
+ _objc_msgSend$setSoftwareUpdateAutoUpdateEnabled:
+ _objc_msgSend$setStolenDeviceProtectionEnabled:
+ _objc_msgSend$setStolenDeviceProtectionStrictModeEnabled:
+ _objc_msgSend$setUnlockWithWatchEnabled:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$setXPCActivity:
+ _objc_msgSend$valueForKey:
- _OBJC_CLASS_$_CKPrettyError
- _OUTLINED_FUNCTION_2
- __34-[SASProximitySession sendAction:]_block_invoke.10
- __58-[SASCloudKitClient fetchRecords:inZone:group:completion:]_block_invoke.18
- _objc_msgSend$itemErrorFromError:forID:
CStrings:
+ "@\"NSMutableDictionary\""
+ "@\"_NSAttributedStringGrammarInflection\""
+ "CKItemErrorForID:"
+ "SASExpressSettingsCreator"
+ "SASProximityInformationDictionaryCoder"
+ "SSID"
+ "SSID_STR"
+ "T@\"NSMutableDictionary\",&,V_dataDictionary"
+ "T@\"NSString\",C,V_fullName"
+ "T@\"_NSAttributedStringGrammarInflection\",&,V_grammarInflection"
+ "_dataDictionary"
+ "_fullName"
+ "_grammarInflection"
+ "appanalytics"
+ "appanalyticsbundleversion"
+ "appearance"
+ "autodownload"
+ "autoupdate"
+ "com.apple.onboarding.analyticsapp"
+ "com.apple.onboarding.analyticsdevice"
+ "com.apple.onboarding.findmy"
+ "com.apple.onboarding.locationservices"
+ "com.apple.onboarding.siri"
+ "createExpressSettingsUsingDictionary:"
+ "dataDictionary"
+ "dataUsingEncoding:"
+ "deviceanalytics"
+ "deviceanalyticsbundleversion"
+ "deviceclass"
+ "displayzoom"
+ "feminine"
+ "filevault"
+ "findmy"
+ "findmybundleversion"
+ "fullName"
+ "grammarInflection"
+ "initWithDictionary:"
+ "locationServices"
+ "locationServicesbundleversion"
+ "lowercaseString"
+ "masculine"
+ "mutableCopy"
+ "neuter"
+ "producttype"
+ "productversion"
+ "screentime"
+ "setDataDictionary:"
+ "setFullName:"
+ "setGender:"
+ "setGrammarInflection:"
+ "setGrammarInflectionGender:"
+ "setValue:forKey:"
+ "setWiFiPassword:"
+ "setWiFiSSID:"
+ "setXPCActivity:"
+ "siri"
+ "siribundleversion"
+ "siridatasharing"
+ "sirivoicetrigger"
+ "stolendeviceprotection"
+ "stolendeviceprotectionstrictmode"
+ "unlockwithwatch"
+ "valueForKey:"
+ "walletdata"
+ "watchmigrationdata"
- "itemErrorFromError:forID:"

```
