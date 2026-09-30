## IMAP

> `/System/Library/PrivateFrameworks/VisualVoicemail.framework/IMAP.framework/IMAP`

```diff

-901.0.0.0.0
-  __TEXT.__text: 0xb0f7c
+902.0.0.0.0
+  __TEXT.__text: 0xb11a8
   __TEXT.__auth_stubs: 0x1aa0
   __TEXT.__objc_methlist: 0xaa9c
   __TEXT.__const: 0x2c8
-  __TEXT.__gcc_except_tab: 0xbd8c
-  __TEXT.__cstring: 0x73d4
-  __TEXT.__oslogstring: 0x4715
+  __TEXT.__gcc_except_tab: 0xbde4
+  __TEXT.__cstring: 0x73eb
+  __TEXT.__oslogstring: 0x47ca
   __TEXT.__ustring: 0x14d0
   __TEXT.__unwind_info: 0x4378
   __TEXT.__objc_classname: 0xffe
-  __TEXT.__objc_methname: 0x16034
+  __TEXT.__objc_methname: 0x16064
   __TEXT.__objc_methtype: 0x30ac
-  __TEXT.__objc_stubs: 0x11c00
+  __TEXT.__objc_stubs: 0x11c20
   __DATA_CONST.__got: 0xbe8
   __DATA_CONST.__const: 0x2eb0
   __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f70
+  __DATA_CONST.__objc_selrefs: 0x5f78
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3b0
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0xd68
   __AUTH_CONST.__const: 0xdf8
-  __AUTH_CONST.__cfstring: 0x9980
-  __AUTH_CONST.__objc_const: 0x12af8
+  __AUTH_CONST.__cfstring: 0x99a0
+  __AUTH_CONST.__objc_const: 0x12b18
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1540
-  __DATA.__objc_ivar: 0xad4
+  __DATA.__objc_ivar: 0xad8
   __DATA.__data: 0xae0
-  __DATA.__bss: 0x330
+  __DATA.__bss: 0x338
   __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__bss: 0x1b8

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6BF398F5-7C48-3BDA-A22F-A7503703FC6F
+  UUID: 92EE6600-28FE-3C0B-87B8-24923693AC56
   Functions: 4109
-  Symbols:   14569
-  CStrings:  7756
+  Symbols:   14572
+  CStrings:  7763
 
Symbols:
+ _OBJC_IVAR_$_MFActivityMonitor._instanceID
+ _g_instance_id
+ _objc_msgSend$updateSelectedMessages:withMailbox:
Functions:
~ -[MFLibraryIMAPStore _fetchMessagesWithArguments:idRange:onConnection:synchronize:limit:topUIDToCompact:topKnownUID:success:examinedRange:fetchableUIDsFound:preserveUID:numFetchedUIDs:] : 4124 -> 4216
~ -[MFMailMessageStore fetchMobileSynchronously:preservingUID:options:] : 936 -> 1316
~ -[MFActivityMonitor init] : 196 -> 224
~ -[MFActivityMonitor description] : 324 -> 380
CStrings:
+ "#I %s%s[FetchActivity] Search for UIDs [%@] returned %lu items (success=%@)"
+ "#I [fetchMobileSynchronously] begin [mailbox:%@]"
+ "#I [fetchMobileSynchronously] completed [%@ messages]"
+ "#I [fetchMobileSynchronously] fetchNumMessages completed [tries %d, result %ld]"
+ "_instanceID"
+ "ivm.%lu (%@) [%@]"
+ "ivm.%lu [%@]"
+ "updateSelectedMessages:withMailbox:"
- "#I %s%s[FetchActivity] Search for recent UIDs returned %lu items (success=%@)"
- "[%@] %@"

```
