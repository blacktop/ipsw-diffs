## Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1686.3.0.0.0
-  __TEXT.__text: 0x10008
+1689.3.0.0.0
+  __TEXT.__text: 0x100c4
   __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_stubs: 0x2f00
+  __TEXT.__objc_stubs: 0x2f20
   __TEXT.__objc_methlist: 0x9e4
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__objc_methname: 0x4725
+  __TEXT.__objc_methname: 0x4779
   __TEXT.__cstring: 0x74b
-  __TEXT.__oslogstring: 0x4ec
+  __TEXT.__oslogstring: 0x53e
   __TEXT.__objc_classname: 0x150
-  __TEXT.__objc_methtype: 0xf98
+  __TEXT.__objc_methtype: 0xfa8
   __TEXT.__unwind_info: 0x2d0
-  __DATA_CONST.__const: 0x920
+  __DATA_CONST.__const: 0x940
   __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__auth_got: 0x328
-  __DATA_CONST.__got: 0x918
+  __DATA_CONST.__got: 0x920
   __DATA.__objc_const: 0xb70
-  __DATA.__objc_selrefs: 0xfd0
+  __DATA.__objc_selrefs: 0xfd8
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x3c8

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 198
-  Symbols:   401
-  CStrings:  783
+  Functions: 199
+  Symbols:   402
+  CStrings:  785
 
Symbols:
+ _OBJC_CLASS_$_PKFinanceKitForegroundHook
CStrings:
+ "PBKSceneDelegate: PKFinanceKitForegroundHook notifyWalletDidForeground failed: %@"
+ "notifyWalletDidForegroundWithCompletionHandler:"
+ "presentBillSplitWithImage:receiptData:recipientAddresses:conversationIdentifier:sessionIdentifier:mode:completion:"
+ "presentPeerPaymentBillSplitWithImage:receiptData:recipientAddresses:conversationIdentifier:sessionIdentifier:mode:"
+ "v72@0:8@\"UIImage\"16@\"NSData\"24@\"NSArray\"32@\"NSString\"40@\"NSString\"48q56@?<v@?B>64"
+ "v72@0:8@16@24@32@40@48q56@?64"
- "presentBillSplitWithImage:receiptData:recipientAddresses:conversationIdentifier:mode:completion:"
- "presentPeerPaymentBillSplitWithImage:receiptData:recipientAddresses:conversationIdentifier:mode:"
- "v64@0:8@\"UIImage\"16@\"NSData\"24@\"NSArray\"32@\"NSString\"40q48@?<v@?B>56"
- "v64@0:8@16@24@32@40q48@?56"
```
