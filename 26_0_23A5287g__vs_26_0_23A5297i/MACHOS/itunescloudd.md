## itunescloudd

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/Support/itunescloudd`

```diff

-4025.100.115.0.0
-  __TEXT.__text: 0x140dc8
+4025.100.124.0.0
+  __TEXT.__text: 0x1415c8
   __TEXT.__auth_stubs: 0x1220
   __TEXT.__objc_stubs: 0x155c0
-  __TEXT.__objc_methlist: 0xb39c
+  __TEXT.__objc_methlist: 0xb3ac
   __TEXT.__dlopen_cstrs: 0x705
   __TEXT.__const: 0x340
-  __TEXT.__gcc_except_tab: 0x5918
-  __TEXT.__oslogstring: 0x29268
+  __TEXT.__gcc_except_tab: 0x5970
+  __TEXT.__oslogstring: 0x29552
   __TEXT.__objc_classname: 0x2668
-  __TEXT.__objc_methname: 0x2195f
+  __TEXT.__objc_methname: 0x21949
   __TEXT.__objc_methtype: 0x463e
-  __TEXT.__cstring: 0x1073c
-  __TEXT.__unwind_info: 0x3998
+  __TEXT.__cstring: 0x10850
+  __TEXT.__unwind_info: 0x39a0
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__auth_got: 0x920
   __DATA_CONST.__got: 0xfd8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x5c38
-  __DATA_CONST.__cfstring: 0xc280
+  __DATA_CONST.__const: 0x5c88
+  __DATA_CONST.__cfstring: 0xc2c0
   __DATA_CONST.__objc_classlist: 0x838
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x178

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 18791916-4D8C-3904-AE6D-F5F22931F3A3
-  Functions: 4925
+  UUID: CFF3DAED-09DE-3E36-9868-18F4DB1AA0D6
+  Functions: 4927
   Symbols:   822
-  CStrings:  10842
+  CStrings:  10857
 
CStrings:
+ "%{public}@ Could not load subscription status (error=%{public}@, status=%{public}@)- will rety the operation later"
+ "%{public}@ Encountered error fetching user social profile; keeping cached ICMusicUserProfile: %{public}@. error=%{public}@"
+ "%{public}@ Fetching watchKit configuration"
+ "%{public}@ Finished artwork import"
+ "%{public}@ Finished fetching bag for storefront details"
+ "%{public}@ Finished fetching bag for storefront details error=%{public}@"
+ "%{public}@ Finished fetching watchKit configuration"
+ "%{public}@ Finished fetching watchKit configuration error=%{public}@"
+ "%{public}@ Finished gathering user state info"
+ "%{public}@ Finished updating user social profile: %{public}@"
+ "%{public}@ Finished updating user social profile: %{public}@ error=%{public}@"
+ "%{public}@ Not running operation..."
+ "%{public}@ _buildUserStateFromUserIdentity completed. userState=%{public}@"
+ "%{public}@ _buildUserStateFromUserIdentity completed. userState=%{public}@ error=%{public}@"
+ "SELECT entity_pid FROM artwork_token WHERE entity_pid"
+ "SELECT item_pid FROM item WHERE album_artist_pid = ? AND in_my_library = 1"
+ "SELECT item_pid FROM item WHERE item_artist_pid = ? AND in_my_library = 1"
+ "SELECT store_id FROM album_artist LEFT OUTER JOIN artwork_token ON album_artist_pid = entity_pid AND entity_type = ? AND artwork_type = ? AND artwork_source_type = ? WHERE store_id != 0 AND EXISTS (SELECT item_pid from item where item.album_artist_pid = album_artist.album_artist_pid AND in_my_library = 1)"
+ "SELECT store_id FROM item_artist LEFT OUTER JOIN artwork_token ON item_artist_pid = entity_pid AND entity_type = ? AND artwork_type = ? AND artwork_source_type = ? WHERE store_id != 0 AND EXISTS (SELECT item_pid from item where item.item_artist_pid = item_artist.item_artist_pid AND in_my_library = 1)"
+ "Skipping bulk artist artwork update because its not allowed with current conditions"
+ "_canRunOperation"
- "%{public}@ Encountered error fetching bag. error=%{public}@"
- "%{public}@ Encountered error fetching user social profile. Keeping cached ICMusicUserProfile: %{public}@. error=%{public}@"
- "%{public}@ Encountered error fetching user social profile. error=%{public}@"
- "%{public}@ Not running operation"
- "SELECT entity_pid FROM artwork_token LEFT OUTER JOIN artwork USING (artwork_token) WHERE artwork_token.artwork_source_type = ? AND relative_path != '' AND entity_pid"
- "SELECT store_id FROM album_artist LEFT OUTER JOIN artwork_token ON album_artist_pid = entity_pid AND entity_type = ? AND artwork_type = ? AND artwork_source_type = ? WHERE store_id != 0"
- "SELECT store_id FROM item_artist LEFT OUTER JOIN artwork_token ON item_artist_pid = entity_pid AND entity_type = ? AND artwork_type = ? AND artwork_source_type = ? WHERE store_id != 0"
- "_canRunOperationWithCompletionHandler:"

```
