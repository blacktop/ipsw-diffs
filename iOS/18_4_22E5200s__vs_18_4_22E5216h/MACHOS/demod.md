## demod

> `/usr/libexec/demod`

```diff

-1445.100.72.0.1
-  __TEXT.__text: 0xde73c
+1445.100.86.0.0
+  __TEXT.__text: 0xdfc50
   __TEXT.__auth_stubs: 0x1b00
-  __TEXT.__objc_stubs: 0x18300
-  __TEXT.__objc_methlist: 0xbc6c
-  __TEXT.__const: 0x226
-  __TEXT.__gcc_except_tab: 0x4608
-  __TEXT.__cstring: 0xe6ca
-  __TEXT.__objc_methname: 0x1c358
-  __TEXT.__oslogstring: 0x17f4c
-  __TEXT.__objc_classname: 0x157a
-  __TEXT.__objc_methtype: 0x369d
+  __TEXT.__objc_stubs: 0x18580
+  __TEXT.__objc_methlist: 0xbd7c
+  __TEXT.__const: 0x21e
+  __TEXT.__gcc_except_tab: 0x4738
+  __TEXT.__cstring: 0xe96a
+  __TEXT.__objc_methname: 0x1c667
+  __TEXT.__oslogstring: 0x1828c
+  __TEXT.__objc_classname: 0x15a0
+  __TEXT.__objc_methtype: 0x36bd
   __TEXT.__swift5_typeref: 0x63
   __TEXT.__swift5_capture: 0x38
   __TEXT.__constg_swiftt: 0x38

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x31b8
+  __TEXT.__unwind_info: 0x3218
   __TEXT.__eh_frame: 0xf8
   __DATA_CONST.__auth_got: 0xd90
-  __DATA_CONST.__got: 0xc78
+  __DATA_CONST.__got: 0xc98
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x2b10
-  __DATA_CONST.__cfstring: 0xd300
-  __DATA_CONST.__objc_classlist: 0x660
+  __DATA_CONST.__const: 0x2be8
+  __DATA_CONST.__cfstring: 0xd400
+  __DATA_CONST.__objc_classlist: 0x668
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x3b0
+  __DATA_CONST.__objc_superrefs: 0x3b8
   __DATA_CONST.__objc_intobj: 0x4c8
-  __DATA_CONST.__objc_arraydata: 0x818
-  __DATA_CONST.__objc_arrayobj: 0x3d8
+  __DATA_CONST.__objc_arraydata: 0x830
+  __DATA_CONST.__objc_arrayobj: 0x408
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x166c0
-  __DATA.__objc_selrefs: 0x6fe0
-  __DATA.__objc_ivar: 0x9f8
-  __DATA.__objc_data: 0x4020
-  __DATA.__data: 0x2698
-  __DATA.__bss: 0x510
+  __DATA.__objc_const: 0x16b18
+  __DATA.__objc_selrefs: 0x7090
+  __DATA.__objc_ivar: 0xa00
+  __DATA.__objc_data: 0x4070
+  __DATA.__data: 0x26f8
+  __DATA.__bss: 0x520
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
+  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5165
-  Symbols:   868
-  CStrings:  9647
+  Functions: 5194
+  Symbols:   872
+  CStrings:  9708
 
Symbols:
+ _OBJC_CLASS_$_UAFAssetSetManager
+ ___NSArray0__struct
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
CStrings:
+ "!\x11"
+ "%s - Completion called"
+ "%s - Device is not opted-in to Apple Intelligence.  Skip waitForGMAvailability"
+ "%s - called"
+ "-[MSDAssetUpdater downloadAssetsWithError:]_block_invoke"
+ "-[MSDAssetUpdater downloadSiriAssetsWithError:]_block_invoke"
+ "-[MSDUAFUpdater downloadAllAssetsFromUAFWithCompletion:]"
+ "-[MSDUAFUpdater downloadAssetsFromUAFForSubscribers:withCompletion:]"
+ "-[MSDUAFUpdater downloadSiriAssetsFromUAFWithCompletion:]"
+ ".GlobalPreferences"
+ "@\"<MSDUAFInterfaceProtocol>\""
+ "@\"UAFAssetSetManager\""
+ "AI opt-in value doesn't exist in the global preferences domain, setting the opt-in value to NO."
+ "Applying the opt-in value \"%@\" to the device"
+ "Checking whether Siri assets are available..."
+ "Demo Device does not support OOB Asset Updates at this time"
+ "Demo devices do not support OOB Asset updates at this time"
+ "Error hit! Error: %ld %@"
+ "Failed to query %du / %du assets"
+ "MSDUAFInterfaceProtocol"
+ "MSDUAFUpdater"
+ "Not toggling the Pallas URL!  Device is not a verified demo device."
+ "Read a valid opt-in value from the global preferences domain: %d"
+ "Siri asset downloads hit an error!"
+ "Siri assets have now become available!"
+ "Siri assets not available yet.  Sleeping for %d minutes before retry.  %ld retries left."
+ "T@\"<MSDUAFInterfaceProtocol>\",&,V_uafConnection"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_uafDownloadQueue"
+ "T@\"UAFAssetSetManager\",&,V_UAFAssetSetManager"
+ "Timed out of checking if assets are available this instance! %ld checks remaining."
+ "Timed out while waiting %dm for Siri assets to download"
+ "UAF download complete!"
+ "UAF download progress %ld / %ld, (%ld%%)"
+ "UAFAssetSetManager"
+ "Waited %d minutes.  Siri assets still unavailable!"
+ "_UAFAssetSetManager"
+ "_uafConnection"
+ "_uafDownloadQueue"
+ "areSiriUODAssetsAvailable:"
+ "assistantIsEnabled"
+ "checkSiriAssetsAvailable"
+ "collectAllSubscribersRequiredForAppleIntelligence"
+ "collectAllSubscribersRequiredForSiri"
+ "com.apple.MobileStoreDemo.UAFDownloadQueue"
+ "com.apple.csf.gm.toggle"
+ "com.apple.siri.assistant"
+ "com.apple.siri.intelligenceengine"
+ "completedBytes"
+ "completedPercent"
+ "downloadAllAssetsFromUAFWithCompletion:"
+ "downloadAssetsFromUAFForSubscribers:withCompletion:"
+ "downloadAssetsWithError failed"
+ "downloadAssetsWithError:"
+ "downloadSiriAssetsFromUAFWithCompletion:"
+ "downloadSiriAssetsWithError:"
+ "handleSiriAssetsWithError failed"
+ "handleSiriAssetsWithError:"
+ "initWithAssetSetManager:"
+ "initWithUAFConnection:"
+ "migrateOptInValue"
+ "model-catalog"
+ "setUAFAssetSetManager:"
+ "setUafConnection:"
+ "setUafDownloadQueue:"
+ "totalBytes"
+ "uafConnection"
+ "uafDownloadQueue"
+ "updateAssetsForSubscribers:policies:queue:detailedProgress:completion:"
+ "v16@?0@\"UAFAssetSetStatus\"8"
- "!\x12"
- "%s - ChangeSettings has new 'AssetQueryFrequency' set."
- "%s - Device has no GM assets.  Skip checkAvailability"
- "@\"MSDAssetUpdater\""
- "Failed to query %lu / %lu assets"
- "T@\"MSDAssetUpdater\",&,V_assetUpdater"
- "_assetUpdater"
- "assetUpdater"
- "queryAndDownloadAssetsWithForceGMAssetTypes:withError failed"
- "setAssetUpdater:"

```
