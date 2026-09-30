## CoreRecents

> `/System/Library/PrivateFrameworks/CoreRecents.framework/Versions/A/CoreRecents`

```diff

-1212.0.0.0.0
-  __TEXT.__text: 0x837c
+1212.500.41.0.0
+  __TEXT.__text: 0x85a8
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0xbfc
+  __TEXT.__objc_methlist: 0xd84
   __TEXT.__cstring: 0x918
   __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x4c
   __TEXT.__oslogstring: 0x2b5
-  __TEXT.__unwind_info: 0x360
+  __TEXT.__unwind_info: 0x388
   __TEXT.__objc_classname: 0x151
   __TEXT.__objc_methname: 0x2452
   __TEXT.__objc_methtype: 0x69f

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa20
+  __DATA_CONST.__objc_selrefs: 0xaa8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
   __AUTH_CONST.__auth_got: 0x1d0
   __AUTH_CONST.__const: 0x630
   __AUTH_CONST.__cfstring: 0xca0
-  __AUTH_CONST.__objc_const: 0x1490
+  __AUTH_CONST.__objc_const: 0x11c8
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x90
   __DATA.__data: 0x198

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: DCFB6783-67A6-3A4E-BC7F-E352ED8816BC
-  Functions: 308
-  Symbols:   953
+  UUID: 6A12110F-2BEF-3FD1-891F-F0FE3633FAF1
+  Functions: 329
+  Symbols:   976
   CStrings:  782
 
Symbols:
+ +[CRLogging client].cold.1
+ +[CRLogging log].cold.1
+ +[CRRecentContactsLibrary _recentEventForGroupMembers:displayName:date:weight:metadata:options:].cold.1
+ +[CRRecentContactsLibrary _recentEventForGroupMembers:displayName:date:weight:metadata:options:].cold.2
+ +[CRRecentContactsLibrary _recentEventForGroupMembers:displayName:date:weight:metadata:options:].cold.3
+ +[CRRecentContactsLibrary defaultInstance].cold.1
+ +[CRRecentContactsLibrary groupMemberWithAddress:displayName:kind:].cold.1
+ +[CRRecentContactsLibrary groupMemberWithAddress:displayName:kind:].cold.2
+ -[CRRecentContact enumerateArchivablePropertiesWithBlock:].cold.1
+ -[CRRecentContact initWithAddress:displayName:kind:recentDate:recentsDomain:].cold.1
+ -[CRRecentContact initWithAddress:displayName:kind:recentDate:recentsDomain:].cold.2
+ -[CRRecentContact initWithAddress:displayName:kind:recentDate:recentsDomain:].cold.3
+ -[CRRecentContact initWithMembers:displayName:recentDate:recentsDomain:].cold.1
+ -[CRRecentContact initWithMembers:displayName:recentDate:recentsDomain:].cold.2
+ -[CRRecentContactsLibrary _recordContactEvents:recentsDomain:sendingAddress:source:userInitiated:completion:].cold.1
+ -[CRRecentContactsLibrary _searchRecentsUsingQuery:completion:].cold.1
+ -[NSString(CoreRecentsUtilities) cr_copyStringByDecodingIDNAInRange:].cold.1
+ -[NSString(CoreRecentsUtilities) cr_copyStringByEncodingIDNAInRange:].cold.1
+ -[NSString(CoreRecentsUtilities) cr_lowercaseStringWithStandardLocale].cold.1
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2

```
