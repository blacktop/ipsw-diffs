## com.apple.quicklook.ThumbnailsAgent

> `/System/Library/Frameworks/QuickLookThumbnailing.framework/Support/com.apple.quicklook.ThumbnailsAgent`

```diff

-185.0.0.0.0
-  __TEXT.__text: 0x14c0
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0x640
-  __TEXT.__objc_methlist: 0x164
+186.2.2.0.0
+  __TEXT.__text: 0x1778
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x760
+  __TEXT.__objc_methlist: 0x194
   __TEXT.__const: 0x70
   __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0x9d4
-  __TEXT.__objc_methtype: 0x414
-  __TEXT.__cstring: 0xcd
-  __TEXT.__oslogstring: 0x96
+  __TEXT.__objc_methname: 0xb9c
+  __TEXT.__objc_methtype: 0x42d
+  __TEXT.__cstring: 0x100
+  __TEXT.__oslogstring: 0xcb
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__unwind_info: 0xc4
-  __DATA_CONST.__auth_got: 0x1a8
+  __TEXT.__unwind_info: 0xd4
+  __DATA_CONST.__auth_got: 0x1d0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x40
+  __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x788
-  __DATA.__objc_selrefs: 0x220
-  __DATA.__objc_classrefs: 0x78
+  __DATA.__objc_const: 0x7e8
+  __DATA.__objc_selrefs: 0x270
+  __DATA.__objc_classrefs: 0x88
   __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x10
+  __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   __DATA.__bss: 0x18

   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/QuickLookSupport.framework/QuickLookSupport
   - /System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 82D62FE6-1FBA-3AFA-A463-AF3EB354902C
-  Functions: 41
-  Symbols:   78
-  CStrings:  164
+  UUID: 8D73BB9C-6767-310B-9007-15FEBC967DDD
+  Functions: 46
+  Symbols:   85
+  CStrings:  186
 
Symbols:
+ _CFRelease
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_QLTGeneratorThumbnailRequest
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ _objc_enumerationMutation
+ _objc_getProperty
+ _objc_setProperty_atomic
- _objc_retain_x4
CStrings:
+ "\x13"
+ "@\"NSString\""
+ "B"
+ "Could not find application identifier for pid %d: %@"
+ "RD13622867.com.apple.finder"
+ "T@\"NSString\",&,V_clientApplicationIdentifier"
+ "TB,V_clientApprovedForAllFiles"
+ "_clientApplicationIdentifier"
+ "_clientApprovedForAllFiles"
+ "addObject:"
+ "application-identifier"
+ "clientApplicationIdentifier"
+ "clientApprovedForAllFiles"
+ "countByEnumeratingWithState:objects:count:"
+ "generateSuccessiveThumbnailRepresentationsForGeneratorRequests:completionHandler:"
+ "initWithCapacity:"
+ "initWithRequest:generationHandler:"
+ "isEqualToString:"
+ "setClientApplicationIdentifier:"
+ "setClientApprovedForAllFiles:"
+ "v20@0:8B16"
- "\x12"

```
