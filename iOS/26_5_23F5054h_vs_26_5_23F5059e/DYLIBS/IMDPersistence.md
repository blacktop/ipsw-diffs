## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1450.600.43.2.1
-  __TEXT.__text: 0x2624cc
-  __TEXT.__auth_stubs: 0x4eb0
-  __TEXT.__objc_methlist: 0x7f24
-  __TEXT.__const: 0xc858
-  __TEXT.__cstring: 0x48b14
-  __TEXT.__oslogstring: 0x1e776
+1450.600.53.2.3
+  __TEXT.__text: 0x2642a0
+  __TEXT.__auth_stubs: 0x4ec0
+  __TEXT.__objc_methlist: 0x7f74
+  __TEXT.__const: 0xc888
+  __TEXT.__cstring: 0x48b64
+  __TEXT.__oslogstring: 0x1e816
   __TEXT.__gcc_except_tab: 0xb678
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x30a
-  __TEXT.__swift5_typeref: 0x3f68
+  __TEXT.__swift5_typeref: 0x3fb8
   __TEXT.__swift5_capture: 0x1284
-  __TEXT.__constg_swiftt: 0x585c
+  __TEXT.__constg_swiftt: 0x5864
   __TEXT.__swift5_builtin: 0x2a8
   __TEXT.__swift5_reflstr: 0x3249
   __TEXT.__swift5_fieldmd: 0x359c

   __TEXT.__swift_as_ret: 0xb0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x9568
-  __TEXT.__eh_frame: 0x8ab0
+  __TEXT.__unwind_info: 0x95a8
+  __TEXT.__eh_frame: 0x8b88
   __TEXT.__objc_classname: 0x28fa
-  __TEXT.__objc_methname: 0x1ba34
-  __TEXT.__objc_methtype: 0x4607
-  __TEXT.__objc_stubs: 0x13b20
+  __TEXT.__objc_methname: 0x1bb54
+  __TEXT.__objc_methtype: 0x4627
+  __TEXT.__objc_stubs: 0x13c60
   __DATA_CONST.__got: 0x18e8
   __DATA_CONST.__const: 0x8228
   __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x57d0
+  __DATA_CONST.__objc_selrefs: 0x5820
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x2e0
-  __AUTH_CONST.__auth_got: 0x2768
-  __AUTH_CONST.__const: 0xadd0
-  __AUTH_CONST.__cfstring: 0x12420
-  __AUTH_CONST.__objc_const: 0x11968
+  __DATA_CONST.__objc_arraydata: 0x300
+  __AUTH_CONST.__auth_got: 0x2770
+  __AUTH_CONST.__const: 0xadd8
+  __AUTH_CONST.__cfstring: 0x12480
+  __AUTH_CONST.__objc_const: 0x11998
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x22b0
   __AUTH.__data: 0x4c20
-  __DATA.__objc_ivar: 0x4c8
+  __DATA.__objc_ivar: 0x4cc
   __DATA.__data: 0x34c0
   __DATA.__bss: 0xae78
   __DATA.__common: 0x210

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A6D92DBA-1E8B-364B-A9C4-62ABE3A57DBC
-  Functions: 11709
+  UUID: 88B37552-A572-31EF-AD09-C71E648A4E90
+  Functions: 11737
   Symbols:   2648
-  CStrings:  12830
+  CStrings:  12854
 
CStrings:
+ " c.chat_identifier LIKE  ? "
+ "!#"
+ "@88@0:8B16q20@28Q36B44B48B52B56@60B68@72@80"
+ "AdditionalReasons"
+ "C24@0:8@16"
+ "Cached chat info was provided for deleting chat GUID %@, but it contained no identifiers. Falling back to database lookup"
+ "ChatMetadata"
+ "SELECT DISTINCT c.rowid, c.chat_identifier\nFROM chat c\nINNER JOIN chat_message_join cmj ON cmj.chat_id = c.rowid\nWHERE"
+ "SELECT c.rowid, c.chat_identifier\nFROM chat c\nWHERE "
+ "T@\"NSDictionary\",&,N,V_chatMetadata"
+ "Unable to pre-fetch the group ID and chat identifier for chat being deleted with GUID %@"
+ "_arrayForKey:"
+ "_chatMetadata"
+ "_dictionaryForKey:"
+ "_initForReindexing:reason:bgstLane:migrationRequirements:preflight:ignoreRejections:ignoreThrottle:forceDeferral:laneOverride:needsTimeSensitiveEvaluation:additionalReasons:chatMetadata:"
+ "_numberForKey:"
+ "addChatMetadataForGUID:style:groupIDs:chatIdentifiers:"
+ "c.rowid"
+ "chatIdentifiersForChatGUID:"
+ "chatMetadata"
+ "cm"
+ "deleteChatGUIDs:context:completionHandler:"
+ "groupIDsForChatGUID:"
+ "hasMetadataForChatWithGUID:"
+ "setChatMetadata:"
+ "styleForChatGUID:"
+ "v44@0:8@16C24@28@36"
- "!\""
- "@80@0:8B16q20@28Q36B44B48B52B56@60B68@72"
- "Failed to check siblings for chat ROWID %lld: %@"
- "SELECT DISTINCT c.rowid\nFROM chat c\nINNER JOIN chat_message_join cmj ON cmj.chat_id = c.rowid\nWHERE c.chat_identifier = ? OR c.chat_identifier LIKE ?\nORDER BY c.rowid ASC;"
- "_initForReindexing:reason:bgstLane:migrationRequirements:preflight:ignoreRejections:ignoreThrottle:forceDeferral:laneOverride:needsTimeSensitiveEvaluation:additionalReasons:"
- "deleteChatGUIDs:reason:completionHandler:"

```
