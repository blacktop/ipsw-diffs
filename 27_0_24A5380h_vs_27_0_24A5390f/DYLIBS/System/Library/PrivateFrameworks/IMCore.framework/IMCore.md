## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/IMCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1486.100.5.2.1
-  __TEXT.__text: 0x2fe854
+1487.100.6.2.2
+  __TEXT.__text: 0x2fcdc0
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0x14c
-  __TEXT.__objc_methlist: 0x18d1c
+  __TEXT.__objc_methlist: 0x18d4c
   __TEXT.__const: 0x116f0
-  __TEXT.__gcc_except_tab: 0x12088
-  __TEXT.__cstring: 0x13515
-  __TEXT.__oslogstring: 0x240eb
+  __TEXT.__gcc_except_tab: 0x1193c
+  __TEXT.__cstring: 0x13405
+  __TEXT.__oslogstring: 0x23b3b
   __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x184
   __TEXT.__swift5_typeref: 0x39ae

   __TEXT.__swift_as_ret: 0x130
   __TEXT.__swift_as_cont: 0x2e0
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0xc478
+  __TEXT.__unwind_info: 0xc390
   __TEXT.__eh_frame: 0x72b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5878
+  __DATA_CONST.__const: 0x58a0
   __DATA_CONST.__objc_classlist: 0x908
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x578
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xea90
+  __DATA_CONST.__objc_selrefs: 0xeaa8
   __DATA_CONST.__objc_protorefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x5b8
   __DATA_CONST.__objc_arraydata: 0xa8
-  __DATA_CONST.__got: 0x2880
+  __DATA_CONST.__got: 0x2878
   __AUTH_CONST.__const: 0xc3f8
-  __AUTH_CONST.__cfstring: 0xba80
-  __AUTH_CONST.__objc_const: 0x22198
+  __AUTH_CONST.__cfstring: 0xbaa0
+  __AUTH_CONST.__objc_const: 0x221d0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x21a8
+  __AUTH_CONST.__auth_got: 0x21a0
   __AUTH.__objc_data: 0x4020
   __AUTH.__data: 0x2d20
-  __DATA.__objc_ivar: 0x12b8
+  __DATA.__objc_ivar: 0x12bc
   __DATA.__data: 0x64f8
   __DATA.__bss: 0x1eae0
   __DATA.__common: 0x7e0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15208
-  Symbols:   2691
-  CStrings:  5052
+  Functions: 15211
+  Symbols:   2689
+  CStrings:  5023
 
Symbols:
- _IMRegisterForSiriSuggestionsInAppSettingChanges
- _IMSiriSuggestionsInAppSettingChangedNotification
CStrings:
+ "-[IMChatRegistry(IMChatRegistry_DaemonIncoming) historyQuery:chatID:services:finishedWithResult:limit:hasMessagesBefore:hasMessagesAfter:]"
+ "IMPLUGIN_SKIPCOLLABORATIONINITIATION_KEY"
- "%s Adding %lu identifiers to coalesced fetch"
- "%s: %ld identifiers need save state fetch"
- "-[IMChatRegistry(IMChatRegistry_DaemonIncoming) historyQuery:chatID:services:finishedWithResult:limit:]"
- "-[IMPhotoLibraryPersistenceManager cachedCountOfSyndicationIdentifiersSavedToSystemPhotoLibrary:shouldFetchAndNotifyAsNeeded:didStartFetch:]"
- "-[IMPhotoLibraryPersistenceManager fetchInfoForSyndicationIdentifiersSavedToSystemPhotoLibrary:completion:]"
- "-[IMSWHighlightCenterController initWithAppIdentifier:]"
- "Broadcasting changes to %lu listeners"
- "CoreAutomation"
- "Fetching %lu identifiers that weren't cached"
- "Finished fetching identifiers that weren't cached. Notifying listeners. identifiersNeedingFetch count: %lu"
- "IMHandle+Utilities: equivalentToRecipients - self or recipient array has duplicate values! self: %@; recipients: %@"
- "IMPhotoLibraryPersistenceManager -- syndicationIdentifiersPendingFetch cleared before fetch could begin, this is an invalid state"
- "IMSWHighlightCenterController"
- "Invalidating cache"
- "No more active sessions, unregistering all listeners and clearing caches"
- "Not allowing IMPhotoLibraryPersistenceManager to be created."
- "Not flushing save state cache as there were no deletions"
- "Not unregistering listener because it's already not listening %p"
- "Photo library changed, will invalidate %d"
- "Received photoLibraryDidChange: notification"
- "Registering IMPhotoLibraryPersistenceManager as a system photo library change observer"
- "Registering active session with GUID %@"
- "Registering as photo library persistence change listener %p"
- "Unregistering all persistence manager listeners"
- "Unregistering as photo library persistence change listener %p"
- "Unregistering listener %p"
- "Unregistering session with GUID %@ remaining sessions active %lu"
- "_handleSiriSuggestionsInAppSettingChanged"
- "groupParticipantsWithGroupID incoming ID %@ "
- "groupParticipantsWithGroupID resulting chat %@ "
- "groupParticipantsWithGroupID resulting participants %@ "
```
