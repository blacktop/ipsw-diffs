## Messages

> `/System/iOSSupport/System/Library/Frameworks/Messages.framework/Versions/A/Messages`

```diff

-1402.400.131.1.3
-  __TEXT.__text: 0x2628c
+1402.500.181.1.1
+  __TEXT.__text: 0x26340
   __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_methlist: 0x37a4
+  __TEXT.__objc_methlist: 0x46e8
   __TEXT.__const: 0x3e6
   __TEXT.__gcc_except_tab: 0x1fc
   __TEXT.__cstring: 0x1c37

   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xb38
+  __TEXT.__unwind_info: 0xb80
   __TEXT.__objc_classname: 0x701
-  __TEXT.__objc_methname: 0xa65f
-  __TEXT.__objc_methtype: 0x2bae
-  __TEXT.__objc_stubs: 0x6920
+  __TEXT.__objc_methname: 0xa69a
+  __TEXT.__objc_methtype: 0x2bf2
+  __TEXT.__objc_stubs: 0x68e0
   __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0x5f8
+  __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20e8
+  __DATA_CONST.__objc_selrefs: 0x2498
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x4b8
   __AUTH_CONST.__const: 0x2e0
   __AUTH_CONST.__cfstring: 0x1720
-  __AUTH_CONST.__objc_const: 0x7408
+  __AUTH_CONST.__objc_const: 0x57f8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x40

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9DF59386-733B-3A08-83C1-1C668EF374A2
-  Functions: 1337
-  Symbols:   3361
+  UUID: 68BF85EA-79B5-3885-99F4-ACA422D57A26
+  Functions: 1355
+  Symbols:   3376
   CStrings:  2441
 
Symbols:
+ +[MSSticker _isHEICSupported].cold.1
+ +[NSURL(MessagesAdditions) __ms_cachesDirectory].cold.1
+ +[NSXPCInterface(MessageComposeExtension) __mf_messageComposerExtensionInterface].cold.1
+ +[NSXPCInterface(MessageComposeExtension) __mf_messageComposerHostInterface].cold.1
+ +[_MSExtensionGlobalState sharedInstance].cold.1
+ +[_MSPresentationState isRunningInCameraContext].cold.1
+ +[_MSStickerSendManager sharedInstance].cold.1
+ +[_MSTempFileManager sharedInstance].cold.1
+ -[MSMessagesAppViewController _presentAlertWithTitle:message:buttonTitle:image:completion:]
+ -[_MSMessageAppBundleContext presentAlertWithTitle:message:buttonTitle:image:completion:]
+ -[_MSMessageAppBundleHostContext _presentAlertWithTitle:message:buttonTitle:image:completion:]
+ -[_MSMessageAppContext presentAlertWithTitle:message:buttonTitle:image:completion:]
+ -[_MSMessageAppExtensionContext presentAlertWithTitle:message:buttonTitle:image:completion:]
+ -[_MSMessageAppExtensionHostContext _presentAlertWithTitle:message:buttonTitle:image:completion:]
+ GCC_except_table105
+ GCC_except_table127
+ GCC_except_table137
+ GCC_except_table52
+ _MSMainBundleIdentifier.cold.1
+ _OUTLINED_FUNCTION_5
+ __block_literal_global.132
+ __block_literal_global.265
+ _objc_msgSend$_presentAlertWithTitle:message:buttonTitle:image:completion:
+ _objc_msgSend$presentAlertWithTitle:message:buttonTitle:image:completion:
+ ms_defaultLog.cold.1
+ ms_traceLog.cold.1
- GCC_except_table104
- GCC_except_table128
- GCC_except_table138
- GCC_except_table53
- __block_literal_global.130
- __block_literal_global.151
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_Messages
- _objc_msgSend$childViewControllers
- _objc_msgSend$convertRect:fromView:
- _objc_msgSend$initialFrameBeforeAppearance
- _objc_msgSend$rootViewController
CStrings:
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Messages_iosmac/ChatKit/Messages/Messages/Source/Extension/MSMessage.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Messages_iosmac/ChatKit/Messages/Messages/Source/Extension/MSMessagesAppViewController.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Messages_iosmac/ChatKit/Messages/Messages/Source/StickerBrowser/MSSticker.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/Messages_iosmac/ChatKit/Messages/Messages/Source/StickerBrowser/MSStickerView.m"
+ "_presentAlertWithTitle:message:buttonTitle:image:completion:"
+ "presentAlertWithTitle:message:buttonTitle:image:completion:"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"UIImage\"40@?<v@?>48"
- "/AppleInternal/Library/BuildRoots/5c0393f9-de33-11ef-b07a-ca56a3f92201/Library/Caches/com.apple.xbs/Sources/Messages_iosmac/ChatKit/Messages/Messages/Source/Extension/MSMessage.m"
- "/AppleInternal/Library/BuildRoots/5c0393f9-de33-11ef-b07a-ca56a3f92201/Library/Caches/com.apple.xbs/Sources/Messages_iosmac/ChatKit/Messages/Messages/Source/Extension/MSMessagesAppViewController.m"
- "/AppleInternal/Library/BuildRoots/5c0393f9-de33-11ef-b07a-ca56a3f92201/Library/Caches/com.apple.xbs/Sources/Messages_iosmac/ChatKit/Messages/Messages/Source/StickerBrowser/MSSticker.m"
- "/AppleInternal/Library/BuildRoots/5c0393f9-de33-11ef-b07a-ca56a3f92201/Library/Caches/com.apple.xbs/Sources/Messages_iosmac/ChatKit/Messages/Messages/Source/StickerBrowser/MSStickerView.m"
- "childViewControllers"
- "convertRect:fromView:"
- "rootViewController"

```
