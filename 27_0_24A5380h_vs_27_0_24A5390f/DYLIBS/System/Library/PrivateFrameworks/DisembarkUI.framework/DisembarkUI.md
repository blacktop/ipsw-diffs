## DisembarkUI

> `/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-281.0.0.0.0
-  __TEXT.__text: 0x1f474
-  __TEXT.__objc_methlist: 0x28d8
+282.0.0.0.0
+  __TEXT.__text: 0x1f3b8
+  __TEXT.__objc_methlist: 0x2920
   __TEXT.__const: 0x194
-  __TEXT.__cstring: 0x1e04
+  __TEXT.__cstring: 0x1d54
   __TEXT.__gcc_except_tab: 0x25c
   __TEXT.__oslogstring: 0xda5
   __TEXT.__dlopen_cstrs: 0xc6

   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x10
-  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__unwind_info: 0x7f8
   __TEXT.__eh_frame: 0x180
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a68
+  __DATA_CONST.__objc_selrefs: 0x1a78
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__got: 0x4c8
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x16a0
-  __AUTH_CONST.__objc_const: 0x4fa0
+  __AUTH_CONST.__cfstring: 0x1620
+  __AUTH_CONST.__objc_const: 0x4ff8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x5d8
   __AUTH.__objc_data: 0xf98
   __AUTH.__data: 0x140
-  __DATA.__objc_ivar: 0x2c4
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0xaf0
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 946
-  Symbols:   2558
-  CStrings:  363
+  Functions: 950
+  Symbols:   2565
+  CStrings:  359
 
Symbols:
+ -[DKFindMyProvider setUsePartnerFinancingPrompt:]
+ -[DKFindMyProvider usePartnerFinancingPrompt]
+ -[DKPasscodeViewController viewDidLoad]
+ -[DKScreenTimePasscodeViewController viewDidLoad]
+ _OBJC_IVAR_$_DKFindMyProvider.usePartnerFinancingPrompt
+ _objc_msgSend$setForceSingleColumnLayout:
+ _objc_msgSend$setUsePartnerFinancingPrompt:
+ _objc_msgSend$usePartnerFinancingPrompt
- _objc_msgSend$arrayWithObject:
Functions:
~ -[DKFindMyProvider disableFindMyWithPresentingViewController:completion:] : 784 -> 928
+ -[DKFindMyProvider usePartnerFinancingPrompt]
+ -[DKFindMyProvider setStateChangeBlock:]
~ -[DKIntroViewController viewDidLoad] : 1036 -> 1048
~ -[DKInternetWarningViewController viewDidLoad] : 1588 -> 1600
+ -[DKPasscodeViewController viewDidLoad]
~ -[DKPartnerFinancingConfirmationController viewDidLoad] : 860 -> 872
~ -[DKPromptCloudUploadViewController viewDidLoad] : 432 -> 444
+ -[DKScreenTimePasscodeViewController viewDidLoad]
~ -[DKCloudUploadViewController viewDidLoad] : 612 -> 624
~ -[DKCloudUploadViewController _showUploadFailureAlertForResults:] : 3292 -> 2692
~ ___27-[DKEraseFlow prepareFlow:]_block_invoke_5 : 220 -> 248
CStrings:
+ "BACKUP_DISABLED_ALERT_BODY"
+ "TURN_OFF_FIND_MY_DISCLOSURE_PARTNER_FINANCING"
+ "UNABLE_TO_BACKUP_TITLE"
- "BACKUP_DISABLED_ALERT_MESSAGE"
- "BACKUP_DISABLED_ALERT_MULTIPLE_ACCOUNTS_MESSAGE"
- "BACKUP_DISABLED_ALERT_MULTIPLE_ACCOUNTS_TITLE"
- "BACKUP_DISABLED_ALERT_SINGLE_ACCOUNT_MESSAGE"
- "BACKUP_DISABLED_ALERT_SINGLE_ACCOUNT_TITLE"
- "BACKUP_DISABLED_ALERT_TITLE"
- "BACKUP_NO_INTERNET_ALERT_TITLE"
```
