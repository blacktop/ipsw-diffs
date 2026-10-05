## demod

> `/usr/libexec/demod`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_ivar`
- `__DATA.__data`

```diff

-1871.40.52.0.0
-  __TEXT.__text: 0xf5c44
+1871.40.61.0.0
+  __TEXT.__text: 0xf6a44
   __TEXT.__auth_stubs: 0x2150
-  __TEXT.__objc_stubs: 0x1bb80
-  __TEXT.__objc_methlist: 0xdc8c
+  __TEXT.__objc_stubs: 0x1bd00
+  __TEXT.__objc_methlist: 0xdce4
   __TEXT.__const: 0x538
-  __TEXT.__cstring: 0x115b2
-  __TEXT.__objc_classname: 0x18ea
+  __TEXT.__cstring: 0x11792
+  __TEXT.__objc_classname: 0x18fa
   __TEXT.__objc_methtype: 0x40bb
-  __TEXT.__gcc_except_tab: 0x47f8
-  __TEXT.__oslogstring: 0x1d6bc
-  __TEXT.__objc_methname: 0x2174e
+  __TEXT.__gcc_except_tab: 0x48e4
+  __TEXT.__oslogstring: 0x1d95c
+  __TEXT.__objc_methname: 0x2187d
   __TEXT.__swift5_typeref: 0x11a
   __TEXT.__swift5_capture: 0xcc
   __TEXT.__constg_swiftt: 0x80

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x20
-  __TEXT.__unwind_info: 0x5158
+  __TEXT.__unwind_info: 0x51b0
   __TEXT.__eh_frame: 0x3d0
-  __DATA_CONST.__const: 0x32a0
-  __DATA_CONST.__cfstring: 0xef60
-  __DATA_CONST.__objc_classlist: 0x738
+  __DATA_CONST.__const: 0x3310
+  __DATA_CONST.__cfstring: 0xf040
+  __DATA_CONST.__objc_classlist: 0x740
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_intobj: 0x4c8
-  __DATA_CONST.__objc_arraydata: 0x940
+  __DATA_CONST.__objc_arraydata: 0x948
   __DATA_CONST.__objc_arrayobj: 0x480
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__auth_got: 0x10b8
-  __DATA_CONST.__got: 0xf58
+  __DATA_CONST.__got: 0xf60
   __DATA_CONST.__auth_ptr: 0x198
-  __DATA.__objc_const: 0x19a60
-  __DATA.__objc_selrefs: 0x8348
+  __DATA.__objc_const: 0x19af0
+  __DATA.__objc_selrefs: 0x83a8
   __DATA.__objc_ivar: 0xb40
-  __DATA.__objc_data: 0x48f0
+  __DATA.__objc_data: 0x4940
   __DATA.__data: 0x2a00
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HomeKit.framework/HomeKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6148
-  Symbols:   1066
-  CStrings:  11064
+  Functions: 6162
+  Symbols:   1067
+  CStrings:  11098
 
Symbols:
+ _OBJC_CLASS_$_CSSearchableIndex
CStrings:
+ "%s - Failed to issue CoreSpotlight command %{public}@ - %{public}@"
+ "%s - Successfully issued CoreSpotlight command %{public}@"
+ "%s - alwaysRecognized: %d"
+ "%s - begin-turbo command failed, disabling turbo to be safe"
+ "%s - issuing CoreSpotlight command %{public}@"
+ "+[MSDSpotlightIndexHelper _runCoreSpotlightCommand:withTimeout:]_block_invoke"
+ "+[MSDSpotlightIndexHelper _startNewIndexingForMessages]"
+ "+[MSDSpotlightIndexHelper endTurbo]"
+ "+[MSDSpotlightIndexHelper startTurbo]"
+ "/var/mobile/Library/Preferences/com.apple.tvremoted.plist"
+ "AlwaysRecognized"
+ "Cannot refresh file download credential: no manifest info for the current content update"
+ "DisableAppleIntelligenceAssetsDownload"
+ "DisableAppleIntelligenceAssetsDownload is set, faking successful asset download"
+ "DisableAppleIntelligenceAssetsDownload is set, returning GM availability as YES"
+ "DisableAppleIntelligenceAssetsDownload is set, skipping purge of existing GreyMatter assets"
+ "MSDSpotlightIndexHelper"
+ "No manifest info available to identify the content update."
+ "Timed out while waiting for CoreSpotlight command %{public}@ to complete."
+ "_issueCommand:completionHandler:"
+ "_runCoreSpotlightCommand:withTimeout:"
+ "_startNewIndexingForMessages"
+ "begin-turbo"
+ "boolForKey:"
+ "defaultSearchableIndex"
+ "end-turbo"
+ "endTurbo"
+ "isAlwaysRecognized"
+ "job:com.apple.MobileSMS:NSFileProtectionCompleteUntilFirstUserAuthentication:2:0"
+ "manifestInfoForCredentialRefresh"
+ "refreshIndexingForMessagesWithCompletion:"
+ "setDemoModeRecognizeMyVoice:"
+ "setDemoModeSetupPresets:"
+ "startTurbo"
```
