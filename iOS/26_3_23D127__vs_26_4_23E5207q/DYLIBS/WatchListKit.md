## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-907.30.4.0.0
-  __TEXT.__text: 0x67414
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x705c
+907.40.26.0.0
+  __TEXT.__text: 0x6baf4
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_methlist: 0x708c
   __TEXT.__const: 0x1a4
-  __TEXT.__cstring: 0x7c17
-  __TEXT.__oslogstring: 0x6327
+  __TEXT.__cstring: 0x7c65
+  __TEXT.__oslogstring: 0x645c
   __TEXT.__gcc_except_tab: 0x11b0
-  __TEXT.__unwind_info: 0x1de8
+  __TEXT.__unwind_info: 0x1fa8
   __TEXT.__objc_classname: 0x1321
-  __TEXT.__objc_methname: 0x1079a
+  __TEXT.__objc_methname: 0x10870
   __TEXT.__objc_methtype: 0x1da5
-  __TEXT.__objc_stubs: 0x9de0
-  __DATA_CONST.__got: 0x8f8
+  __TEXT.__objc_stubs: 0x9e80
+  __DATA_CONST.__got: 0x908
   __DATA_CONST.__const: 0x2778
   __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3958
+  __DATA_CONST.__objc_selrefs: 0x3988
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x628
-  __AUTH_CONST.__auth_got: 0x420
+  __AUTH_CONST.__auth_got: 0x3f8
   __AUTH_CONST.__const: 0xe80
-  __AUTH_CONST.__cfstring: 0xa480
-  __AUTH_CONST.__objc_const: 0x11bb8
+  __AUTH_CONST.__cfstring: 0xa520
+  __AUTH_CONST.__objc_const: 0x11bf8
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x19f0
-  __DATA.__objc_ivar: 0xa34
+  __DATA.__objc_ivar: 0xa38
   __DATA.__data: 0x7a0
-  __DATA.__bss: 0x108
+  __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x1bd0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x430
+  __DATA_DIRTY.__bss: 0x440
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2E5C083F-3BD7-3A43-98A2-1497728FF129
-  Functions: 2754
-  Symbols:   10096
-  CStrings:  6470
+  UUID: 33B3E7B4-9548-385D-A075-85E234636593
+  Functions: 2764
+  Symbols:   10129
+  CStrings:  6493
 
Symbols:
+ +[WLKURLBagUtilities utsURLForBagKeyApplyingHostOverrideIfSet:]
+ -[WLKAppLibrary _supportPath]
+ -[WLKChannelDetails appAgeRestrictionRatingValue]
+ -[WLKPlaybackSummary needsIntentDonation]
+ GCC_except_table48
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_TVASURLSessionManagerObjC
+ _OBJC_IVAR_$_WLKChannelDetails._appAgeRestrictionRatingValue
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ ___35-[WLKAppLibrary _refreshAppLibrary]_block_invoke.33
+ ___45-[WLKAppLibrary endIgnoringAppLibraryChanges]_block_invoke.30
+ ___46-[WLKNetworkRequestOperation configureSession]_block_invoke.21
+ ___47-[WLKAppLibrary _handleInvalidationWithReason:]_block_invoke.41
+ ___block_descriptor_48_e8_32s40bs_e35_v24?0"AMSURLRequest"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e59_v32?0"AMSURLRequestEncoder"8"NSURLRequest"16"NSError"24ls48l8s32l8s40l8
+ ___block_literal_global.23
+ ___block_literal_global.44
+ _objc_msgSend$closeFile
+ _objc_msgSend$defaultSession
+ _objc_msgSend$fileHandleForWritingAtPath:
+ _objc_msgSend$host
+ _objc_msgSend$synchronizeFile
+ _objc_msgSend$utsURLForBagKeyApplyingHostOverrideIfSet:
- ___35-[WLKAppLibrary _refreshAppLibrary]_block_invoke.29
- ___45-[WLKAppLibrary endIgnoringAppLibraryChanges]_block_invoke.26
- ___46-[WLKNetworkRequestOperation configureSession]_block_invoke.23
- ___47-[WLKAppLibrary _handleInvalidationWithReason:]_block_invoke.34
- ___block_descriptor_56_e8_32s40s48bs_e35_v24?0"AMSURLRequest"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e59_v32?0"AMSURLRequestEncoder"8"NSURLRequest"16"NSError"24ls56l8s32l8s40l8s48l8
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$setUrlKnownToBeTrusted:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "T@\"NSNumber\",R,N,V_appAgeRestrictionRatingValue"
+ "TeamPageRedesign"
+ "WLKAppLibrary - Error: TVASDefaultSupportPath returned nil"
+ "WLKAppLibrary - Failed to archive app library dictionary data: %@"
+ "WLKAppLibrary - Failed to write app library dictionary data."
+ "WLKPostPlayAutoPlay - The ongoing operation has different settings, remove the ongoing operation."
+ "WLKURLBagUtilities:: URL for given bag key not found in bag: %@"
+ "WLKURLBagUtilities:: updating URL to use base URL override"
+ "_appAgeRestrictionRatingValue"
+ "andromeda"
+ "appAgeRestrictionRatingValue"
+ "applibrarydict"
+ "closeFile"
+ "defaultSession"
+ "fileHandleForWritingAtPath:"
+ "needsIntentDonation"
+ "siriActionsExpirationTime"
+ "synchronizeFile"
+ "utsURLForBagKeyApplyingHostOverrideIfSet:"
+ "video_summary"
- "WLKPostPlayAutoPlay - The ongoing operation has different settings, cancel the ongoing operation."
- "setUrlKnownToBeTrusted:"

```
