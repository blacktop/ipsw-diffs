## VisualUnderstanding

> `/System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding`

```diff

-59.10.0.0.0
-  __TEXT.__text: 0xc6030
-  __TEXT.__auth_stubs: 0x1750
+59.12.1.0.0
+  __TEXT.__text: 0xc0f2c
+  __TEXT.__auth_stubs: 0x1740
   __TEXT.__objc_methlist: 0x26c
-  __TEXT.__const: 0x1e2c
-  __TEXT.__cstring: 0x306c
-  __TEXT.__swift5_typeref: 0x16a4
-  __TEXT.__oslogstring: 0x1ccc
-  __TEXT.__swift5_capture: 0xb2c
-  __TEXT.__swift5_reflstr: 0xd71
+  __TEXT.__const: 0x1e0c
+  __TEXT.__cstring: 0x286c
+  __TEXT.__swift5_typeref: 0x1554
+  __TEXT.__oslogstring: 0x1cdc
+  __TEXT.__swift5_capture: 0x988
+  __TEXT.__swift5_reflstr: 0xd81
   __TEXT.__swift5_assocty: 0x208
-  __TEXT.__constg_swiftt: 0x195c
-  __TEXT.__swift5_fieldmd: 0xf98
+  __TEXT.__constg_swiftt: 0x1998
+  __TEXT.__swift5_fieldmd: 0xfcc
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x114
-  __TEXT.__swift5_types: 0x114
+  __TEXT.__swift5_types: 0x118
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x21f0
-  __TEXT.__eh_frame: 0x4e88
+  __TEXT.__unwind_info: 0x2158
+  __TEXT.__eh_frame: 0x4e28
   __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methname: 0x11c8
+  __TEXT.__objc_methname: 0x11c1
   __TEXT.__objc_methtype: 0x134
-  __DATA_CONST.__got: 0x468
+  __DATA_CONST.__got: 0x458
   __DATA_CONST.__const: 0x400
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c0
+  __DATA_CONST.__objc_selrefs: 0x6b8
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xba8
-  __AUTH_CONST.__auth_ptr: 0x438
-  __AUTH_CONST.__const: 0x3b18
-  __AUTH_CONST.__objc_const: 0x2218
+  __AUTH_CONST.__auth_got: 0xba0
+  __AUTH_CONST.__auth_ptr: 0x418
+  __AUTH_CONST.__const: 0x36e8
+  __AUTH_CONST.__objc_const: 0x2238
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x668
-  __DATA.__data: 0x948
+  __DATA.__data: 0x980
   __DATA.__bss: 0x1f80
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x970
-  __DATA_DIRTY.__data: 0x2238
+  __DATA_DIRTY.__data: 0x2198
   __DATA_DIRTY.__common: 0xc0
   __DATA_DIRTY.__bss: 0x200
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2732
-  Symbols:   446
-  CStrings:  776
+  Functions: 2653
+  Symbols:   418
+  CStrings:  731
 
CStrings:
+ "Error: index store is corrupted (%!s(MISSING)) - resetting"
+ "NOT (noindex:(identifier) IN %!@(MISSING))"
+ "mapping.label != -1 AND mapping.density == -1 AND noindex:(isPrimary) == YES AND noindex:(type) == %!d(MISSING)"
+ "mapping.label == -1 AND noindex:(type) == %!d(MISSING)"
+ "mapping.partition == %!l(MISSING)ld AND noindex:(type) == %!d(MISSING) AND noindex:(embedding) != nil AND noindex:(isPrimary) == YES"
+ "mapping.partition == -1 AND mapping.label == -1 AND noindex:(type) == %!d(MISSING)"
+ "maxSize"
+ "noindex:(identifier) IN %!@(MISSING)"
+ "noindex:(mapping.label) == %!l(MISSING)ld"
+ "size"
- "Error: index store is corrupted - resetting"
- "NOT (identifier IN %!@(MISSING))"
- "com.apple.VisualUnderstanding.ClusteringMetrics"
- "com.apple.VisualUnderstanding.CrossDomainRecognition"
- "com.apple.VisualUnderstanding.ObservationsEntitiesTags"
- "confirmed_person_tags"
- "confirmed_pet_tags"
- "contacts_confirmed_tags"
- "contacts_observations"
- "contacts_secondary_observations"
- "domain"
- "homekit_confirmed_tags"
- "homekit_observations"
- "homekit_secondary_observation"
- "homekit_tag_and_resolved_contacts_entities"
- "mapping.label != -1 AND mapping.density == -1 AND isPrimary == YES AND type == %!d(MISSING)"
- "noindex:(type) == %!d(MISSING) AND mapping.partition == -1"
- "noindex:(type) == %!d(MISSING) AND noindex:(embedding) != nil AND mapping.partition == %!l(MISSING)ld AND noindex:(isPrimary) == YES"
- "observation.isPrimary == false AND observation.client == %!d(MISSING)"
- "observation.isPrimary == false AND observation.client == %!d(MISSING) AND label IN %!@(MISSING)"
- "person_observations"
- "person_precision"
- "person_supervision_tags"
- "person_worst_precision"
- "person_worst_recall"
- "pet_observations"
- "pet_worst_precision"
- "pet_worst_recall"
- "pets_supervision_tags"
- "photos_confirmed_tags"
- "photos_tag_and_confirmed_contacts_entities"
- "photos_tag_and_confirmed_homekit_entities"
- "photos_tag_and_inferred_contacts_entities"
- "photos_tag_and_inferred_homekit_entities"
- "photos_video_faces_secondary_observations"
- "primary_observations"
- "rejected_person_tags"
- "rejected_pet_tags"
- "secondary_observations"
- "secondary_observations_contacts"
- "secondary_observations_contacts_matching_main_clusters"
- "secondary_observations_homekit"
- "secondary_observations_homekit_matching_main_clusters"
- "secondary_observations_photos"
- "secondary_observations_photos_matching_main_clusters"
- "secondary_observations_syndicated"
- "secondary_observations_syndicated_matching_main_clusters"
- "tagged_face_entities"
- "type != %!d(MISSING) AND observation.client == %!d(MISSING) AND observation.mapping.label != -1"
- "type != %!d(MISSING) AND observation.mapping.label != -1 AND observation.embedding != nil AND observation.type == %!d(MISSING)"
- "type == %!d(MISSING) AND client == %!d(MISSING) AND isPrimary == NO"
- "type == %!d(MISSING) AND client == %!d(MISSING) AND isPrimary == NO AND asset != nil"
- "type == %!d(MISSING) AND observation.client == %!d(MISSING)"
- "type == %!d(MISSING) AND observation.type == %!d(MISSING)"
- "type == %!d(MISSING) AND observation.type == %!d(MISSING) AND resolved == YES"

```
