## ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

-3217.0.4.0.0
-  __TEXT.__text: 0x1ee10
+3218.0.9.0.0
+  __TEXT.__text: 0x1efe8
   __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_stubs: 0x5c00
-  __TEXT.__objc_methlist: 0x1b08
+  __TEXT.__objc_stubs: 0x5c20
+  __TEXT.__objc_methlist: 0x1b10
   __TEXT.__const: 0x210
   __TEXT.__gcc_except_tab: 0x5a0
-  __TEXT.__cstring: 0x2a48
-  __TEXT.__objc_methname: 0x8888
-  __TEXT.__oslogstring: 0x1754
+  __TEXT.__cstring: 0x2b47
+  __TEXT.__objc_methname: 0x891c
+  __TEXT.__oslogstring: 0x1786
   __TEXT.__objc_classname: 0x4c9
   __TEXT.__objc_methtype: 0x1a22
-  __TEXT.__unwind_info: 0x790
+  __TEXT.__unwind_info: 0x798
   __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0xb18
-  __DATA_CONST.__cfstring: 0x1c40
+  __DATA_CONST.__const: 0xaf8
+  __DATA_CONST.__cfstring: 0x1cc0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc8

   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x53e0
-  __DATA.__objc_selrefs: 0x1a08
+  __DATA.__objc_selrefs: 0x1a10
   __DATA.__objc_ivar: 0x2bc
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x968

   - /System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 770
+  Functions: 772
   Symbols:   244
-  CStrings:  2013
+  CStrings:  2019
 
CStrings:
+ "%s There's already a view on screen (presentedBanner: %@, presentedRemoteAlertViewController: %@) and status isn't visible, nothing to do here"
+ "-[WFBannerManager queue_dismissRemoteAlertViewControllerWithReason:]"
+ "-[WFBannerManager queue_updateStateWithReason:]_block_invoke_7"
+ "Remote Alert Action Interface"
+ "T@\"UIViewController\",&,N,V_presentedRemoteAlertViewController"
+ "T{os_unfair_lock_s=I},R,N,V_presentedRemoteAlertViewControllerLock"
+ "_presentedRemoteAlertViewController"
+ "_presentedRemoteAlertViewControllerLock"
+ "action presentation cancelled"
+ "dismiss presented content was called for the currently presented action UI"
+ "dismissing action UI scene"
+ "presentedRemoteAlertViewController"
+ "presentedRemoteAlertViewControllerLock"
+ "queue_dismissRemoteAlertViewControllerWithReason:"
+ "setPresentedRemoteAlertViewController:"
+ "we just dismissed action UI, updating state: %@"
- "%s There's already a presentable on screen (%@) and status isn't visible, nothing to do here"
- "-[WFBannerManager queue_updateStateWithReason:]_block_invoke_6"
- "Legacy Action Interface"
- "T@\"UIViewController\",&,N,V_remoteViewController"
- "T{os_unfair_lock_s=I},R,N,V_remoteViewControllerLock"
- "_remoteViewController"
- "_remoteViewControllerLock"
- "remoteViewController"
- "remoteViewControllerLock"
- "setRemoteViewController:"

```
