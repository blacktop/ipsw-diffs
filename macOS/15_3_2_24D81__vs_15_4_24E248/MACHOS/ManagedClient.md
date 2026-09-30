## ManagedClient

> `/System/Library/CoreServices/ManagedClient.app/Contents/MacOS/ManagedClient`

```diff

-1755.1.0.0.0
-  __TEXT.__text: 0xcacec
-  __TEXT.__auth_stubs: 0x2430
-  __TEXT.__objc_stubs: 0x7380
-  __TEXT.__objc_methlist: 0x1d00
+1770.4.14.0.0
+  __TEXT.__text: 0xc9648
+  __TEXT.__auth_stubs: 0x23e0
+  __TEXT.__objc_stubs: 0x7340
+  __TEXT.__objc_methlist: 0x21cc
   __TEXT.__const: 0x1f1
-  __TEXT.__gcc_except_tab: 0x290c
-  __TEXT.__cstring: 0x3ad15
-  __TEXT.__oslogstring: 0x31764
-  __TEXT.__objc_classname: 0x4b7
-  __TEXT.__objc_methtype: 0x1546
-  __TEXT.__objc_methname: 0x7759
-  __TEXT.__unwind_info: 0x1d78
-  __DATA_CONST.__auth_got: 0x1228
-  __DATA_CONST.__got: 0x8c8
+  __TEXT.__gcc_except_tab: 0x297c
+  __TEXT.__cstring: 0x3a66e
+  __TEXT.__oslogstring: 0x31091
+  __TEXT.__objc_classname: 0x4a7
+  __TEXT.__objc_methtype: 0x1532
+  __TEXT.__objc_methname: 0x771e
+  __TEXT.__unwind_info: 0x1d48
+  __DATA_CONST.__auth_got: 0x1200
+  __DATA_CONST.__got: 0x8c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1740
-  __DATA_CONST.__cfstring: 0xaf40
+  __DATA_CONST.__cfstring: 0xaec0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0xf0
-  __DATA_CONST.__objc_arrayobj: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x148
+  __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x2a70
-  __DATA.__objc_selrefs: 0x2020
+  __DATA.__objc_const: 0x20e0
+  __DATA.__objc_selrefs: 0x2200
   __DATA.__objc_ivar: 0x170
   __DATA.__objc_data: 0x6e0
   __DATA.__data: 0x21a

   - /usr/lib/libcups.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 6099597A-5B97-378D-8876-D6EBA17ED11F
-  Functions: 3005
-  Symbols:   873
-  CStrings:  10822
+  UUID: 401E657C-DC29-336E-ABC6-9AF6F7ED0F9B
+  Functions: 3048
+  Symbols:   867
+  CStrings:  10757
 
Symbols:
+ _malloc_type_calloc
- _NSFileTypeSymbolicLink
- _acl_free
- _acl_get_file
- _acl_init
- _acl_set_file
- _acl_to_text
- _acl_valid
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "MCX.completeMCXLogin unable to allocate memory for user ID information"
+ "MCX.completeMCXLogin user ID information is empty, allocating memory"
+ "_isAppleIntelligenceRestricted"
+ "allowExternalIntelligenceIntegrations"
+ "allowExternalIntelligenceIntegrationsSignIn"
+ "allowGenmoji"
+ "allowMailSmartReplies"
+ "allowMailSummary"
+ "allowNotesTranscription"
+ "allowNotesTranscriptionSummary"
+ "allowSafariSummary"
+ "mcxSvr_recompositeprofilewithinfo WORKQUEUE adding new item. Now has %ld items."
- " %d"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/Network/Servers/"
- "B40@0:8@16@24B32B36"
- "LoginRedirection"
- "LogoutRedirection"
- "MCX -postCompositeMCXRedirector"
- "MCX -postCompositeMCXRedirector actionArray = \n%s"
- "MCX -postCompositeMCXRedirector: isServerHome = %d"
- "MCX -postCompositeMCXRedirector: path=\"%s\""
- "MCX -postCompositeMCXRedirector: rawPath=\"%s\", userHome=\"%s\", userName=\"%s\""
- "MCX -postCompositeMCXRedirector: unknown action: \"%s\""
- "MCX -postCompositeMCXRedirector:%s AGAIN [fm removeItemAtPath:\"%s\"] = %ld (%s)"
- "MCX -postCompositeMCXRedirector:%s AGAIN removing path:\"%s\" = %ld (%s)"
- "MCX -postCompositeMCXRedirector:%s AGAIN removing symlink:\"%s\" = %ld (%s)"
- "MCX -postCompositeMCXRedirector:%s AGAIN removing:\"%s\" = %ld (%s)"
- "MCX -postCompositeMCXRedirector:%s [fm createDirectoryAtPath:\"%s\" withIntermediateDirectories:TRUE] = %ld (%s)"
- "MCX -postCompositeMCXRedirector:%s [fm createSymbolicLinkAtPath:\"%s\" pathContent:\"%s\"] %ld (%s)"
- "MCX -postCompositeMCXRedirector:%s [fm createSymbolicLinkAtPath:\"%s\" pathContent:\"%s\"] = %ld (%s)"
- "MCX -postCompositeMCXRedirector:%s [fm moveItemAtPath:\"%s\" toPath:\"%s\"]"
- "MCX -postCompositeMCXRedirector:%s [fm moveItemAtPath:\"%s\" toPath:\"%s\"] FAILED"
- "MCX -postCompositeMCXRedirector:%s [fm removeItemAtPath:\"%s\"] = %ld (%s)"
- "MCX -postCompositeMCXRedirector:%s bad %s: \"%s\" -> \"%s\""
- "MCX -postCompositeMCXRedirector:%s path \"%s\" is not symbolic link."
- "MCX -postCompositeMCXRedirector:%s path \"%s\" not found."
- "MCX -postCompositeMCXRedirector:%s removing \"%s\""
- "MCX -postCompositeMCXRedirector:%s removing path:\"%s\" = %ld (%s)"
- "MCX -postCompositeMCXRedirector:%s removing symlink \"%s\""
- "MCX -postCompositeMCXRedirector:%s removing:\"%s\""
- "MCX -postCompositeMCXRedirector:%s removing:\"%s\" FAILED"
- "MCX -postCompositeMCXRedirector:%s renamed \"%s\" to \"%s\""
- "MCX -postCompositeMCXRedirector:%s: could not find original with name \"%s [1-20]\""
- "MCX -postCompositeMCXRedirector:acl_set_file = %d"
- "MCX -postCompositeMCXRedirector:action deleteSymLinkAndRestore; path %s"
- "MCX -postCompositeMCXRedirector=%d,  ACL: %s "
- "OtherRedirection"
- "RedirectorPrefs"
- "action"
- "com.apple.MCXRedirector"
- "deleteAndCreateSymLink"
- "deletePath"
- "deleteSymLinkAndRestore"
- "destPath"
- "fileType"
- "mcxSvr_recompositeprofilewithinfo WORKQUEUE adding new item.  Now has %ld items."
- "postCompositeMCXRedirector:userHome:login:logout:"
- "renameAndCreateSymLink"

```
