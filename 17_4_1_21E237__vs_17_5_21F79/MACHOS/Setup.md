## Setup

> `/Applications/Setup.app/Setup`

```diff

-5116.0.0.0.0
-  __TEXT.__text: 0x20ae00
+5125.0.0.0.0
+  __TEXT.__text: 0x20c420
   __TEXT.__auth_stubs: 0x21f0
-  __TEXT.__objc_stubs: 0x22a40
-  __TEXT.__objc_methlist: 0x14290
-  __TEXT.__cstring: 0xdc52
-  __TEXT.__objc_methname: 0x3374f
+  __TEXT.__objc_stubs: 0x22ae0
+  __TEXT.__objc_methlist: 0x142b8
+  __TEXT.__cstring: 0xdd9f
+  __TEXT.__objc_methname: 0x337ed
   __TEXT.__const: 0x13f8
   __TEXT.__constg_swiftt: 0x116c
   __TEXT.__swift5_typeref: 0xbb0

   __TEXT.__objc_classname: 0x3185
   __TEXT.__objc_methtype: 0x9edb
   __TEXT.__swift5_capture: 0xac0
-  __TEXT.__gcc_except_tab: 0x3150
-  __TEXT.__oslogstring: 0xdafa
-  __TEXT.__dlopen_cstrs: 0xfaa
-  __TEXT.__unwind_info: 0x84c0
+  __TEXT.__gcc_except_tab: 0x3148
+  __TEXT.__oslogstring: 0xdd06
+  __TEXT.__dlopen_cstrs: 0xff6
+  __TEXT.__unwind_info: 0x84f8
   __TEXT.__eh_frame: 0xbd8
   __DATA_CONST.__auth_got: 0x1110
-  __DATA_CONST.__got: 0xa28
+  __DATA_CONST.__got: 0xa20
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x64a8
-  __DATA_CONST.__cfstring: 0xa8a0
+  __DATA_CONST.__const: 0x6508
+  __DATA_CONST.__cfstring: 0xa980
   __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x450
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_classrefs: 0x1368
+  __DATA_CONST.__objc_classrefs: 0x1360
   __DATA_CONST.__objc_superrefs: 0x778
   __DATA_CONST.__objc_arraydata: 0x3a0
   __DATA_CONST.__objc_arrayobj: 0x78

   __DATA_CONST.__objc_intobj: 0x2d0
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA.__objc_const: 0x3fd38
-  __DATA.__objc_selrefs: 0xa070
+  __DATA.__objc_selrefs: 0xa098
   __DATA.__objc_ivar: 0x1930
   __DATA.__objc_data: 0x7b58
   __DATA.__data: 0x4018
-  __DATA.__bss: 0x1ae0
+  __DATA.__bss: 0x1af0
   __DATA.__common: 0xc8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10218
-  Symbols:   1358
-  CStrings:  12523
+  Functions: 10234
+  Symbols:   1356
+  CStrings:  12548
 
Symbols:
+ _kDMCErrorDetailsSUInfoKey
- _OBJC_CLASS_$_MCProfile
- _kDMCErrorDetailsBuildVersionKey
- _kDMCErrorDetailsOSVersionKey
CStrings:
+ "BuddyCloudConfigController.m"
+ "Class getSDMDMConfiguratorClass(void)_block_invoke"
+ "Diagnostics display mode potentially including apps (via eligibility)"
+ "Diagnostics display mode potentially including apps (via mismatch)"
+ "Error enrolling in beta program: %@"
+ "Failed to set UI complete for cloud configuration. Error: %{public}@"
+ "Failed to store profile data with error: %{public}@"
+ "May  2 2024"
+ "OSVersion"
+ "RequireBetaProgram"
+ "Required Beta Program but no valid token provided, skipping beta enrollment"
+ "Required Beta Program: %@"
+ "SDMDMConfigurator"
+ "Storing voice trigger enabled in settings manager, because voice trigger prompt was shown"
+ "Successfully enrolled in beta program"
+ "Token"
+ "Transfer Data Migration Wired Both with Home Button"
+ "Transfer Data Migration Wired Both without Home Button"
+ "Transfer Data Migration Wired with Home Button"
+ "Transfer Data Migration Wired without Home Button"
+ "_completeCloudConfig"
+ "_determineDisplayModeShouldPotentiallyIncludeApps"
+ "_storeProfileDataAndCompleteDisclosure:"
+ "cloudConfigDidFinishFromViewController:wasApplied:"
+ "cloudConfigurationUIDidCompleteWasApplied:completionHandler:"
+ "didShowVoiceTriggerPrompt"
+ "enrollInProgramWithMDMToken:completion:"
+ "showRetrievalError:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/Seeding.framework/Seeding"
+ "storeProfileData:"
+ "storeProfileData:completion:"
+ "void *SeedingLibrary(void)"
- "Mar  9 2024"
- "Transfer Options Migrate Wired"
- "cloudConfigDidFinishWasApplied:"
- "installationWarnings"
- "profileWithData:fileName:outError:"
- "storeProfileData:configurationSource:purpose:"
- "transitionToConsentViewControllerFromController:profileData:"

```
