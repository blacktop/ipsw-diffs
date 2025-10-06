## CloudSharingUI

> `/System/Library/PrivateFrameworks/CloudSharingUI.framework/CloudSharingUI`

```diff

-215.1.3.1.0
-  __TEXT.__text: 0x4c688
-  __TEXT.__auth_stubs: 0x1c70
-  __TEXT.__objc_methlist: 0x7dc
+215.1.6.0.0
+  __TEXT.__text: 0x4c700
+  __TEXT.__auth_stubs: 0x1c80
+  __TEXT.__objc_methlist: 0x7fc
   __TEXT.__const: 0x2e0e
-  __TEXT.__cstring: 0x1c31
-  __TEXT.__oslogstring: 0xb63
+  __TEXT.__cstring: 0x1c61
+  __TEXT.__oslogstring: 0xc63
   __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__swift5_typeref: 0x4978
   __TEXT.__constg_swiftt: 0x1434
-  __TEXT.__swift5_reflstr: 0xaa4
-  __TEXT.__swift5_fieldmd: 0xa64
+  __TEXT.__swift5_reflstr: 0xac4
+  __TEXT.__swift5_fieldmd: 0xa70
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x340
   __TEXT.__swift5_capture: 0x640

   __TEXT.__unwind_info: 0x1278
   __TEXT.__eh_frame: 0xd24
   __TEXT.__objc_classname: 0x16b
-  __TEXT.__objc_methname: 0x1ee1
-  __TEXT.__objc_methtype: 0x7e4
-  __TEXT.__objc_stubs: 0xbe0
-  __DATA_CONST.__got: 0x6d8
-  __DATA_CONST.__const: 0x378
+  __TEXT.__objc_methname: 0x1f95
+  __TEXT.__objc_methtype: 0x7ff
+  __TEXT.__objc_stubs: 0xc00
+  __DATA_CONST.__got: 0x6e8
+  __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7f0
+  __DATA_CONST.__objc_selrefs: 0x810
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xe48
+  __DATA_CONST.__objc_superrefs: 0x20
+  __AUTH_CONST.__auth_got: 0xe50
   __AUTH_CONST.__const: 0x1730
   __AUTH_CONST.__cfstring: 0x140
-  __AUTH_CONST.__objc_const: 0x17b8
+  __AUTH_CONST.__objc_const: 0x1838
   __AUTH.__objc_data: 0x8a0
-  __AUTH.__data: 0x1740
-  __DATA.__objc_ivar: 0x48
+  __AUTH.__data: 0x1750
+  __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x14e8
   __DATA.__bss: 0x1ef8
-  __DATA.__common: 0x130
+  __DATA.__common: 0x138
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B81FDE72-9BB0-3BAB-8BD8-F1E124636227
-  Functions: 1803
-  Symbols:   1298
-  CStrings:  632
+  UUID: BB48B226-9F8A-32ED-882D-D769832EAF13
+  Functions: 1808
+  Symbols:   1315
+  CStrings:  646
 
Symbols:
+ -[CSAddParticipantsViewController initWithCKShare:containerSetupInfo:fileURL:collaborationOptionsGroups:headerImageData:headerTitle:loadingText:supplementaryText:primaryButtonText:secondaryButtonText:].cold.1
+ -[CSAddParticipantsViewController sandboxingURLWrapperError]
+ -[CSAddParticipantsViewController sandboxingURLWrapper]
+ -[CSAddParticipantsViewController setSandboxingURLWrapper:]
+ -[CSAddParticipantsViewController setSandboxingURLWrapperError:]
+ _OBJC_CLASS_$_FPSandboxingURLWrapper
+ _OBJC_IVAR_$_CSAddParticipantsViewController._sandboxingURLWrapper
+ _OBJC_IVAR_$_CSAddParticipantsViewController._sandboxingURLWrapperError
+ ___46-[CSAddParticipantsViewController viewDidLoad]_block_invoke.8
+ ___46-[CSAddParticipantsViewController viewDidLoad]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ __dispatch_main_q
+ _dispatch_async
+ _objc_msgSend$sandboxingURLWrapper
+ _objc_msgSend$sandboxingURLWrapperError
+ _objc_msgSend$setSandboxingURLWrapper:
+ _objc_msgSend$wrapperWithURL:readonly:error:
- -[CSAddressingViewController initWithViewModel:userDidClickPrimaryButton:userDidClickSecondaryButton:userDidClickShowContactPicker:userDidChangeAddresses:]
- ___46-[CSAddParticipantsViewController viewDidLoad]_block_invoke.6
- _objc_msgSend$fileURL
- _objc_msgSend$initWithHeaderImageData:headerTitle:loadingText:supplementaryText:userInfoText:primaryButtonText:secondaryButtonText:userDidClickPrimaryButton:userDidClickSecondaryButton:userDidClickShowContactPicker:userDidChangeAddresses:
- _objc_msgSend$setFileURL:
CStrings:
+ "@\"FPSandboxingURLWrapper\""
+ "@\"NSError\""
+ "@108@0:8@16@24@32@40@48@56@64B72@?76@?84@?92@?100"
+ "All existing participants will be removed from this share and it’ll be deleted from iCloud Drive on all of their devices."
+ "Created read-only FPSandboxingURLWrapper for URL: %@"
+ "Created read/write FPSandboxingURLWrapper for URL: %@"
+ "Failed to create read-only FPSandboxingURLWrapper for URL: %@"
+ "Failed to create read/write FPSandboxingURLWrapper for URL: %@--trying read-only"
+ "T@\"FPSandboxingURLWrapper\",&,N,V_sandboxingURLWrapper"
+ "T@\"NSError\",&,N,V_sandboxingURLWrapperError"
+ "_sandboxingURLWrapper"
+ "_sandboxingURLWrapperError"
+ "initWithHeaderImageData:headerTitle:loadingText:supplementaryText:userInfoText:primaryButtonText:secondaryButtonText:shouldAllowEmptyAddresses:userDidClickPrimaryButton:userDidClickSecondaryButton:userDidClickShowContactPicker:userDidChangeAddresses:"
+ "sandboxingURLWrapper"
+ "sandboxingURLWrapperError"
+ "setSandboxingURLWrapper:"
+ "setSandboxingURLWrapperError:"
+ "shouldAllowEmptyAddresses"
+ "v24@0:8@\"FPSandboxingURLWrapper\"16"
+ "wrapperWithURL:readonly:error:"
- "@104@0:8@16@24@32@40@48@56@64@?72@?80@?88@?96"
- "@56@0:8@16@?24@?32@?40@?48"
- "All existing participants will be removed from this share and it'll be deleted from iCloud Drive on all of their devices."
- "initWithHeaderImageData:headerTitle:loadingText:supplementaryText:userInfoText:primaryButtonText:secondaryButtonText:userDidClickPrimaryButton:userDidClickSecondaryButton:userDidClickShowContactPicker:userDidChangeAddresses:"
- "initWithViewModel:userDidClickPrimaryButton:userDidClickSecondaryButton:userDidClickShowContactPicker:userDidChangeAddresses:"
- "v24@0:8@\"NSURL\"16"

```
