## NotesDataConsumer

> `/System/Library/PrivateFrameworks/ExchangeSync.framework/Versions/A/DataConsumers/NotesDataConsumer.dataconsumer/Contents/MacOS/NotesDataConsumer`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2075.0.0.0.0
-  __TEXT.__text: 0x6e00
+2080.200.31.0.0
+  __TEXT.__text: 0x7278
   __TEXT.__auth_stubs: 0x1c0
-  __TEXT.__objc_stubs: 0x1320
-  __TEXT.__objc_methlist: 0x51c
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x37c
+  __TEXT.__objc_stubs: 0x1400
+  __TEXT.__objc_methlist: 0x534
+  __TEXT.__const: 0x88
+  __TEXT.__gcc_except_tab: 0x3dc
   __TEXT.__cstring: 0xbe
-  __TEXT.__oslogstring: 0x140e
-  __TEXT.__objc_methname: 0x1488
+  __TEXT.__oslogstring: 0x14e1
+  __TEXT.__objc_methname: 0x1608
   __TEXT.__objc_classname: 0x43
   __TEXT.__objc_methtype: 0x394
-  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__unwind_info: 0x1f8
   __DATA_CONST.__const: 0xf8
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0xf0
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__got: 0x98
   __DATA.__objc_const: 0x490
-  __DATA.__objc_selrefs: 0x618
+  __DATA.__objc_selrefs: 0x650
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/ExchangeSync.framework/Versions/A/ExchangeSync
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 98
-  Symbols:   55
-  CStrings:  340
+  Functions: 100
+  Symbols:   58
+  CStrings:  349
 
Symbols:
+ _OBJC_CLASS_$_EXSFeatureFlagManager
+ _OBJC_CLASS_$_EXSNotesEchoSuppression
+ _OBJC_CLASS_$_EXSNotesFolderPlacementPolicy
CStrings:
+ "EXSNotesDataConsumer upsync: note %{public}@ is unchanged since the last sync, treating this local change as our own write echoing back"
+ "changeItemIsTopLevel:messageRootExternalID:notesRootExternalID:graphPathActive:"
+ "graphNotesPathIsActive"
+ "graphSyncEnabled"
+ "isExchangeOnline"
+ "itemDidFailToSync: kind=%{public}@ externalID=%{public}@ error=%{private}@"
+ "lastSyncedPropertiesForNoteWithExternalID:internalID:dataManager:"
+ "localChangeIsEchoForNoteTitle:noteContent:lastSyncedProperties:"
+ "orderingSeedExternalIDWithMessageRoot:notesRoot:graphPathActive:"
+ "topLevelParentExternalIDWithMessageRoot:notesRoot:graphPathActive:"
- "setWithObject:"
```
