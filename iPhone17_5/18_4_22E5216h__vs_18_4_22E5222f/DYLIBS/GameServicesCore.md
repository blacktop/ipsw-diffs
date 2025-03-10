## GameServicesCore

> `/System/Library/PrivateFrameworks/GameServicesCore.framework/GameServicesCore`

```diff

-819.4.37.0.0
-  __TEXT.__text: 0x16de50
-  __TEXT.__auth_stubs: 0x4740
-  __TEXT.__const: 0xed20
-  __TEXT.__swift5_typeref: 0x61d4
-  __TEXT.__swift_as_entry: 0x9ac
-  __TEXT.__swift_as_ret: 0xbdc
-  __TEXT.__cstring: 0x2b3f
-  __TEXT.__oslogstring: 0xc06
-  __TEXT.__constg_swiftt: 0x24c4
-  __TEXT.__swift5_reflstr: 0x1dd6
-  __TEXT.__swift5_fieldmd: 0x26f4
-  __TEXT.__swift5_types: 0x258
-  __TEXT.__swift5_assocty: 0x818
-  __TEXT.__swift5_proto: 0xa00
-  __TEXT.__swift5_acfuncs: 0x870
+819.4.42.2.1
+  __TEXT.__text: 0x18d4d0
+  __TEXT.__auth_stubs: 0x49e0
+  __TEXT.__const: 0x108b0
+  __TEXT.__cstring: 0x2fdf
+  __TEXT.__swift5_typeref: 0x6b6e
+  __TEXT.__swift_as_entry: 0xa2c
+  __TEXT.__swift_as_ret: 0xcac
+  __TEXT.__oslogstring: 0xed7
+  __TEXT.__constg_swiftt: 0x287c
+  __TEXT.__swift5_reflstr: 0x2166
+  __TEXT.__swift5_fieldmd: 0x2dc4
+  __TEXT.__swift5_types: 0x2bc
+  __TEXT.__swift5_assocty: 0x848
+  __TEXT.__swift5_proto: 0xb5c
+  __TEXT.__swift5_acfuncs: 0x8e8
   __TEXT.__swift5_capture: 0x1b0
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x80a0
-  __TEXT.__eh_frame: 0x16158
-  __TEXT.__objc_methname: 0x2b5
-  __DATA_CONST.__got: 0x1070
-  __DATA_CONST.__const: 0x210
-  __DATA_CONST.__objc_classlist: 0xe0
+  __TEXT.__unwind_info: 0x8c70
+  __TEXT.__eh_frame: 0x182c0
+  __TEXT.__objc_methname: 0x2d1
+  __DATA_CONST.__got: 0x1118
+  __DATA_CONST.__const: 0x208
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x110
-  __AUTH_CONST.__auth_got: 0x23a0
-  __AUTH_CONST.__auth_ptr: 0x1660
-  __AUTH_CONST.__const: 0x4d70
-  __AUTH_CONST.__objc_const: 0x20b0
-  __AUTH.__objc_data: 0x6e0
-  __AUTH.__data: 0x27d0
-  __DATA.__data: 0x4dd8
-  __DATA.__bss: 0x13b10
+  __DATA_CONST.__objc_selrefs: 0x120
+  __AUTH_CONST.__auth_got: 0x24f0
+  __AUTH_CONST.__auth_ptr: 0x16b0
+  __AUTH_CONST.__const: 0x59a0
+  __AUTH_CONST.__objc_const: 0x2380
+  __AUTH.__objc_data: 0x730
+  __AUTH.__data: 0x2960
+  __DATA.__data: 0x5458
+  __DATA.__bss: 0x16928
   __DATA.__common: 0x1a0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9094
-  Symbols:   3943
-  CStrings:  415
+  Functions: 9991
+  Symbols:   4320
+  CStrings:  459
 
CStrings:
+ " since supportsPartyCode is true"
+ "Challenge ID: %s has a known definition, skipping refresh."
+ "Done fetching game activity definitions for: %s. Storing enriched definitions..."
+ "Done storing game activity definitions for: %s"
+ "Empty response for bundleID: "
+ "Failed to construct activity store, modelContainerURL is nil."
+ "Failed to describe activity definition for %s"
+ "Failed to handle activity open URL: %@"
+ "Failed to handle activity referral deep link open URL: %@"
+ "Fetching Game Activity Definitions for bundleID: %s [adamID: %s]"
+ "Found unknown deep link referral type in GameActivityStoreV1"
+ "GSGameActivityStore"
+ "In store definitions for %s are empty, falling back to fake data."
+ "In store definitions for %s are empty."
+ "Min players must be defined for GameActivity definition: "
+ "Missing required parameters for persistent store"
+ "Nickname suggestions can only be provided for the authenticated player"
+ "No activities returned for bundleID: %s [adamID: %s]"
+ "No leaderboards or achievements to fetch to enrich activity definitions."
+ "Received a notification with invalid number of referral types: %s"
+ "Unknown type of GameActivityDefinitionFilter"
+ "Unknown type of GameActivityStaticStat"
+ "_TtC16GameServicesCoreP33_81C79D1A55373C705C89347D493FEB0717GameActivityStore"
+ "_TtCV16GameServicesCore19GameActivityStoreV126GameActivityInstanceSchema"
+ "_TtCV16GameServicesCore19GameActivityStoreV128GameActivityDefinitionSchema"
+ "_associatedAchievementDescriptionIDs"
+ "_associatedAchievementDescriptionUUIDs"
+ "_associatedLeaderboardIDs"
+ "_associatedLeaderboardUUIDs"
+ "_defaultProperties"
+ "_details"
+ "_fallbackURL"
+ "_maxPlayers"
+ "_minPlayers"
+ "_playStyle"
+ "_supportsPartyCode"
+ "associatedAchievementDescriptionIDs"
+ "associatedAchievementDescriptionUUIDs"
+ "associatedLeaderboardIDs"
+ "associatedLeaderboardUUIDs"
+ "asynchronous"
+ "defaultProperties"
+ "gk-get-suggested-player-nickname"
+ "leaderboards,achievements"
+ "previousProviderReferenceIdentifier"
+ "relate[activities]"
+ "setIncludedResultKeys:"
+ "synchronous"
+ "unspecified"
- "Failed to create activity store, databaseURL is nil"
- "Found unknown deep link referral type in GameActivityInstanceSchemaV1"
- "GameActivityInstance"
- "Received a notification with multiple referral types: %s"
- "_TtC16GameServicesCore17GameActivityStore"
- "_TtCV16GameServicesCore28GameActivityInstanceSchemaV126GameActivityInstanceSchema"

```
