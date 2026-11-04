## itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-4026.210.1.0.0
-  __TEXT.__text: 0x1751b8
+4026.300.13.0.0
+  __TEXT.__text: 0x174154
   __TEXT.__auth_stubs: 0x1950
-  __TEXT.__objc_stubs: 0x18040
-  __TEXT.__objc_methlist: 0xcb64
+  __TEXT.__objc_stubs: 0x18020
+  __TEXT.__objc_methlist: 0xcb34
   __TEXT.__dlopen_cstrs: 0x705
-  __TEXT.__const: 0x610
-  __TEXT.__cstring: 0x1231b
+  __TEXT.__const: 0x620
+  __TEXT.__cstring: 0x12309
   __TEXT.__objc_classname: 0x29ec
-  __TEXT.__objc_methname: 0x2619b
-  __TEXT.__objc_methtype: 0x4eb1
+  __TEXT.__objc_methname: 0x2613b
+  __TEXT.__objc_methtype: 0x4e99
   __TEXT.__constg_swiftt: 0xf4
   __TEXT.__swift5_typeref: 0xcc
   __TEXT.__swift5_reflstr: 0x4e
   __TEXT.__swift5_fieldmd: 0xa4
   __TEXT.__swift5_capture: 0x8c
-  __TEXT.__oslogstring: 0x3289b
+  __TEXT.__oslogstring: 0x325cb
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift_as_entry: 0x2c

   __TEXT.__swift_as_cont: 0x44
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__gcc_except_tab: 0x516c
-  __TEXT.__unwind_info: 0x5110
+  __TEXT.__unwind_info: 0x50f0
   __TEXT.__eh_frame: 0x6e8
-  __DATA_CONST.__const: 0x6910
+  __DATA_CONST.__const: 0x68f0
   __DATA_CONST.__cfstring: 0xcfe0
   __DATA_CONST.__objc_classlist: 0x8f0
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x678
   __DATA_CONST.__objc_intobj: 0x1020
-  __DATA_CONST.__objc_arraydata: 0x2b8
+  __DATA_CONST.__objc_arraydata: 0x2b0
   __DATA_CONST.__objc_arrayobj: 0x2a0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__auth_got: 0xcb8
   __DATA_CONST.__got: 0x1210
   __DATA_CONST.__auth_ptr: 0xb8
-  __DATA.__objc_const: 0x18320
-  __DATA.__objc_selrefs: 0x70e8
-  __DATA.__objc_ivar: 0xff8
+  __DATA.__objc_const: 0x182f8
+  __DATA.__objc_selrefs: 0x70d8
+  __DATA.__objc_ivar: 0xff4
   __DATA.__objc_data: 0x5a48
   __DATA.__data: 0x15a8
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5783
+  Functions: 5775
   Symbols:   1025
-  CStrings:  10363
+  CStrings:  10350
 
CStrings:
+ "ICDCloudAPNSChannelRegistry - notifying registrants of unsubscribe reason=%{public}@ channels=%{public}@"
+ "Refusing XPC connection %{public}@ from %{public}@[reportedFailure=%{BOOL}u, %d] for %{public}@[%ld]: %{public}@"
+ "UPDATE album SET cloud_channel_name=? WHERE (cloud_channel_name !=? AND release_event_aux_info=? AND is_prerelease=?)"
+ "_notifyChannelsResubscribed:reason:"
+ "_notifyChannelsUnsubscribed:reason:"
+ "_setTimer:tracked:toFireAt:leewayNanos:"
+ "snapshotWithDomain:type:subType:context:detectedProcess:triggerThresholdValues:events:completion:"
+ "v48@0:8@16^d24d32Q40"
+ "\xf0\""
- "@\"NSHashTable\""
- "Fetching catalog-pending push messages across all library channels"
- "ICDCloudAPNSChannelRegistry - connection=%{public}@ now observing all library album channels observerCount=%lu"
- "ICDCloudAPNSChannelRegistry - connection=%{public}@ stopped observing all library album channels observerCount=%lu"
- "ICDCloudAPNSChannelRegistry - not setting observe-all as the connection is nil"
- "ICDCloudAPNSChannelRegistry - not setting observe-all as the feature is unavailable"
- "ICDCloudAPNSChannelRegistry - notifying unsubscribe reason=%{public}@ channels=%{public}@"
- "ICDCloudAPNSChannelRegistry - replaying %lu library-album push(es) to observe-all connection=%{public}@"
- "ICDCloudAPNSChannelRegistry - unable to read pending library-album pushes"
- "Refusing XPC connection %{public}@ from %{public}@[%d] for %{public}@[%ld]: %{public}@."
- "Reporting %d catalog-pending library push message(s)"
- "Reporting nil catalog-pending library push messages; metadata unreadable"
- "UPDATE album SET cloud_channel_name=? WHERE (cloud_channel_name !=? AND is_followed=? AND release_event_aux_info=? AND is_prerelease=?)"
- "_libraryAlbumObserverConnections"
- "_notifyLibraryAlbumObserversChannelsResubscribed:reason:"
- "_notifyLibraryAlbumObserversChannelsUnsubscribed:reason:"
- "_replayLibraryAlbumPushesToConnection:"
- "_setTimer:tracked:toFireAt:"
- "catalogPendingPushMessagesForLibraryChannels"
- "setObservesAllLibraryAlbumChannels:completion:"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "\xf02"
```
