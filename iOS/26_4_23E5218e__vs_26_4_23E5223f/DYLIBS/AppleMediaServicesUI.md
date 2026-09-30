## AppleMediaServicesUI

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI`

```diff

-7.4.21.1.0
-  __TEXT.__text: 0x1e6ef8
+7.4.25.0.0
+  __TEXT.__text: 0x1e7000
   __TEXT.__auth_stubs: 0x4640
-  __TEXT.__objc_methlist: 0x10824
+  __TEXT.__objc_methlist: 0x10844
   __TEXT.__const: 0xcdb4
   __TEXT.__gcc_except_tab: 0x1a08
   __TEXT.__oslogstring: 0xa1db

   __TEXT.__swift_as_entry: 0x194
   __TEXT.__swift_as_ret: 0x1d4
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x8c70
+  __TEXT.__unwind_info: 0x8c68
   __TEXT.__eh_frame: 0x5de0
   __TEXT.__objc_classname: 0x36e4
   __TEXT.__objc_methname: 0x2707f

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9B7E7F32-62B5-30F5-AF82-57AE439F215D
-  Functions: 13516
-  Symbols:   25970
+  UUID: 94F0B049-020C-3268-A75D-06988C31E1D4
+  Functions: 13518
+  Symbols:   25974
   CStrings:  11438
 
Symbols:
+ -[AMSUIDynamicViewController viewDidAppear:]
+ -[AMSUIWebViewController viewDidLoad]
+ GCC_except_table100
+ GCC_except_table107
+ GCC_except_table115
+ GCC_except_table58
+ GCC_except_table93
+ GCC_except_table95
+ GCC_except_table97
+ ___46-[AMSUIWebViewController _applyMappingsToURL:]_block_invoke.84
+ ___46-[AMSUIWebViewController _applyMappingsToURL:]_block_invoke.89
+ ___48-[AMSUIWebViewController _loadRequest:bagValue:]_block_invoke.220
+ ___48-[AMSUIWebViewController _loadRequest:bagValue:]_block_invoke.227
+ ___49-[AMSUIWebViewController _lazyPromiseForPageLoad]_block_invoke.174
+ ___55-[AMSUIWebViewController _lazyPromiseForLoadingSession]_block_invoke.169
+ ___61-[AMSUIWebViewController _handleDialogRequest:pauseTimeouts:]_block_invoke.151
+ ___65-[AMSUIWebViewController _handleEngagementRequest:pauseTimeouts:]_block_invoke.160
+ ___65-[AMSUIWebViewController _lazyPromiseForLoadingRequest:bagValue:]_block_invoke.165
+ ___65-[AMSUIWebViewController _lazyPromiseForLoadingRequest:bagValue:]_block_invoke.166
+ ___67-[AMSUIWebViewController _handleAuthenticateRequest:pauseTimeouts:]_block_invoke.110
+ ___67-[AMSUIWebViewController _handleAuthenticateRequest:pauseTimeouts:]_block_invoke.114
+ ___67-[AMSUIWebViewController _handleAuthenticateRequest:pauseTimeouts:]_block_invoke.129
+ ___67-[AMSUIWebViewController _handleAuthenticateRequest:pauseTimeouts:]_block_invoke.139
- GCC_except_table106
- GCC_except_table114
- GCC_except_table57
- GCC_except_table89
- GCC_except_table94
- GCC_except_table96
- GCC_except_table99
- ___46-[AMSUIWebViewController _applyMappingsToURL:]_block_invoke.82
- ___46-[AMSUIWebViewController _applyMappingsToURL:]_block_invoke.87
- ___48-[AMSUIWebViewController _loadRequest:bagValue:]_block_invoke.218
- ___48-[AMSUIWebViewController _loadRequest:bagValue:]_block_invoke.225
- ___49-[AMSUIWebViewController _lazyPromiseForPageLoad]_block_invoke.172
- ___55-[AMSUIWebViewController _lazyPromiseForLoadingSession]_block_invoke.167
- ___61-[AMSUIWebViewController _handleDialogRequest:pauseTimeouts:]_block_invoke.149
- ___65-[AMSUIWebViewController _handleEngagementRequest:pauseTimeouts:]_block_invoke.158
- ___65-[AMSUIWebViewController _lazyPromiseForLoadingRequest:bagValue:]_block_invoke.163
- ___65-[AMSUIWebViewController _lazyPromiseForLoadingRequest:bagValue:]_block_invoke.164
- ___67-[AMSUIWebViewController _handleAuthenticateRequest:pauseTimeouts:]_block_invoke.106
- ___67-[AMSUIWebViewController _handleAuthenticateRequest:pauseTimeouts:]_block_invoke.112
- ___67-[AMSUIWebViewController _handleAuthenticateRequest:pauseTimeouts:]_block_invoke.125
- ___67-[AMSUIWebViewController _handleAuthenticateRequest:pauseTimeouts:]_block_invoke.135
Functions:
~ -[AMSUIDynamicViewController _setup] : 112 -> 104
~ -[AMSUIDynamicViewController viewDidLoad] : 112 -> 104
+ -[AMSUIDynamicViewController viewDidAppear:]
~ -[AMSUIDynamicViewController _setupContentSize] : 124 -> 156
~ -[AMSUIEngagementTaskViewController viewDidAppear:] : 56 -> 76
~ -[AMSUIEngagementViewController viewDidAppear:] : 56 -> 76
~ -[AMSUIEngagementWrapperViewController _setupContentSize] : 124 -> 156
~ -[AMSUIMessageViewSolariumLayoutContext _updateWithRootFrame:] : 5324 -> 5336
~ -[AMSUIMessageViewSolariumLayoutContext calculateMainContentFrameRootFrame:] : 576 -> 596
~ -[AMSUIWebViewController loadView] : 644 -> 636
+ -[AMSUIWebViewController viewDidLoad]

```
