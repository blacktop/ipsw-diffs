## SpotlightReceiver

> `/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver`

```diff

-2328.7.8.5.0
-  __TEXT.__text: 0x4160
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_methlist: 0x190
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0xb8
-  __TEXT.__cstring: 0x224
+2333.7.0.1.0
+  __TEXT.__text: 0x44f0
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_methlist: 0x204
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x1c8
+  __TEXT.__cstring: 0x262
   __TEXT.__oslogstring: 0x3a1
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_classname: 0x4f
-  __TEXT.__objc_methname: 0xc0c
+  __TEXT.__objc_methname: 0xce5
   __TEXT.__objc_methtype: 0x30e
-  __TEXT.__objc_stubs: 0x9c0
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__objc_stubs: 0xb20
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d0
+  __DATA_CONST.__objc_selrefs: 0x330
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x2c0
-  __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x390
+  __AUTH_CONST.__auth_got: 0x300
+  __AUTH_CONST.__cfstring: 0x80
+  __AUTH_CONST.__objc_const: 0x2a0
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x80
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
+  - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 76
-  Symbols:   201
-  CStrings:  214
+  Functions: 77
+  Symbols:   217
+  CStrings:  222
 
Symbols:
+ _APP_SANDBOX_READ
+ _CPCopyBundleIdentifierAndTeamFromApplicationIdentifier
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_PKManager
+ _PKManagerPlugInBundleIdentifierKey
+ _SecTaskCopySigningIdentifier
+ __Block_object_dispose
+ _kSecEntitlementCoreSpotlightApplicationIdentifier
+ _objc_release_x9
+ _objc_retainAutoreleasedReturnValue
+ _sandbox_extension_issue_file
+ _strlen
+ _xpc_connection_is_extension
CStrings:
+ "application-identifier"
+ "bundleIdentifier"
+ "com.apple.omnisearch."
+ "com.apple.spotlight-indexable"
+ "containingAppForPlugInWithPid:"
+ "containingBundleRecord"
+ "dataWithBytesNoCopy:length:"
+ "defaultManager"
+ "encodeURL:withSandboxExtensionData:"
+ "fileSystemRepresentation"
+ "hasPrefix:"
+ "informationForPlugInWithPid:"
+ "initWithBundleIdentifier:error:"
+ "objectForKeyedSubscript:"
+ "path"
- "encodeURLPreservingSecurityScope:"
- "j"
- "pd"
- "pu"
- "ri"
- "s"
- "searchableItemsDidUpdate:"

```
