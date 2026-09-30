## PhotosFace

> `/System/Library/PrivateFrameworks/PhotosFace.framework/PhotosFace`

```diff

-58.0.0.0.0
-  __TEXT.__text: 0xf5dac
-  __TEXT.__auth_stubs: 0x2330
-  __TEXT.__objc_methlist: 0x50
-  __TEXT.__cstring: 0x3135
-  __TEXT.__swift5_typeref: 0x23a4
-  __TEXT.__const: 0x6420
-  __TEXT.__swift5_reflstr: 0x12be
-  __TEXT.__swift5_assocty: 0x500
-  __TEXT.__constg_swiftt: 0x319c
+66.0.2.0.0
+  __TEXT.__text: 0xe9300
+  __TEXT.__auth_stubs: 0x21c0
+  __TEXT.__cstring: 0x320c
+  __TEXT.__swift5_typeref: 0x2199
+  __TEXT.__swift5_reflstr: 0x1384
+  __TEXT.__swift5_assocty: 0x5c0
+  __TEXT.__const: 0x6318
+  __TEXT.__constg_swiftt: 0x3018
   __TEXT.__swift5_fieldmd: 0x1ca4
-  __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_proto: 0x4e4
-  __TEXT.__swift5_types: 0x260
-  __TEXT.__oslogstring: 0x694
-  __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__swift5_capture: 0x9b4
-  __TEXT.__unwind_info: 0x4928
-  __TEXT.__eh_frame: 0xb880
+  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_mpenum: 0x6c
+  __TEXT.__swift5_proto: 0x4e0
+  __TEXT.__swift5_types: 0x24c
+  __TEXT.__swift5_capture: 0x6fc
+  __TEXT.__swift5_protos: 0x24
+  __TEXT.__oslogstring: 0x6ef
+  __TEXT.__unwind_info: 0x4588
+  __TEXT.__eh_frame: 0xab58
   __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0x590
+  __TEXT.__objc_methname: 0x419
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x468
-  __DATA_CONST.__const: 0x300
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__const: 0x320
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c0
+  __DATA_CONST.__objc_selrefs: 0x128
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1198
-  __AUTH_CONST.__auth_ptr: 0x9e0
-  __AUTH_CONST.__const: 0x4948
-  __AUTH_CONST.__objc_const: 0xe98
-  __AUTH.__objc_data: 0x170
-  __AUTH.__data: 0x1ab8
-  __DATA.__data: 0x4228
-  __DATA.__bss: 0x8ea0
-  __DATA.__common: 0x18
+  __AUTH_CONST.__auth_got: 0x10e0
+  __AUTH_CONST.__auth_ptr: 0xa30
+  __AUTH_CONST.__const: 0x4530
+  __AUTH_CONST.__objc_const: 0xdd0
+  __AUTH.__objc_data: 0x50
+  __AUTH.__data: 0x1410
+  __DATA.__data: 0x3958
+  __DATA.__bss: 0x8220
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__data: 0xd50
+  __DATA_DIRTY.__bss: 0x980
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5133
-  Symbols:   255
-  CStrings:  338
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4896
+  Symbols:   252
+  CStrings:  315
 
Symbols:
+ _OBJC_CLASS_$_PHAsset
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _OBJC_CLASS_$_NSObject
- _OBJC_CLASS_$_PFCStoredPhoto
- _OBJC_CLASS_$_PHObject
- _OBJC_CLASS_$__TtC10PhotosFace18PhotoProcessResult
- _OBJC_METACLASS_$_NSObject
- _OBJC_METACLASS_$__TtC10PhotosFace18PhotoProcessResult
- __swift_stdlib_reportUnimplementedInitializer
- _objc_autoreleaseReturnValue
- _objc_msgSendSuper2
CStrings:
+ "    DELETE FROM stored_layout WHERE photo_id IN ("
+ "    INSERT INTO stored_layout(\n        photo_id,\n        time_position,\n        has_mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height\n    )\n    VALUES\n        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
+ "    INSERT INTO stored_photo(\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        accessibility_description,\n        version\n    )\n    VALUES\n        (?, ?, ?, ?, ?, ?)"
+ "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        has_mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        accessibility_description,\n        version\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    WHERE\n        photo_id not in(SELECT photo_id FROM tracked_gallery_photos UNION SELECT photo_id FROM tracked_shuffle_photos UNION SELECT photo_id FROM tracked_album_photos);"
+ "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        has_mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        accessibility_description,\n        version\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    WHERE \n        photo_id IN ("
+ "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        has_mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        accessibility_description,\n        version,\n        day\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    NATURAL JOIN tracked_album_photos\n    NATURAL JOIN tracked_album\n    WHERE\n        album_id = ?\n        "
+ "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        has_mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        accessibility_description,\n        version,\n        day\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    NATURAL JOIN tracked_album_photos\n    NATURAL JOIN tracked_album\n    WHERE\n        album_id = ?\n        AND day = ?\n        "
+ "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        has_mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        accessibility_description,\n        version,\n        day\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    NATURAL JOIN tracked_gallery_photos\n    NATURAL JOIN tracked_gallery\n    WHERE\n        gallery_id = ?\n        "
+ "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        has_mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        accessibility_description,\n        version,\n        day\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    NATURAL JOIN tracked_gallery_photos\n    NATURAL JOIN tracked_gallery\n    WHERE\n        gallery_id = ?\n        AND day = ? \n        "
+ "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        has_mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        accessibility_description,\n        version,\n        day\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    NATURAL JOIN tracked_shuffle_photos\n    NATURAL JOIN tracked_shuffle\n    WHERE\n        shuffle_id = ?\n        "
+ "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        has_mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        accessibility_description,\n        version,\n        day\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    NATURAL JOIN tracked_shuffle_photos\n    NATURAL JOIN tracked_shuffle\n    WHERE\n        shuffle_id = ?\n        AND day = ?\n        "
+ "    SELECT\n        photo_id,\n        time_position,\n        has_mask_image,\n        version\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    WHERE version = ? AND photo_id IN ("
+ "1_add_photo_version"
+ "3_add_sync_state"
+ "4_add_photo_description"
+ "5_string_to_uuid"
+ "Couldn't find necessary attachment: %!s(MISSING)"
+ "Error while executing migration: %!s(MISSING)."
+ "IgnoreDuetCancellations"
+ "IgnoreSyncCache"
+ "Ignoring error while executing migration: %!s(MISSING)."
+ "Picking %!l(MISSING)d from array of size %!l(MISSING)d, picking from %!l(MISSING)d elements"
+ "ROLLBACK; BEGIN; PRAGMA user_version = "
+ "Saving %!l(MISSING)d photos to disk."
+ "TargetGalleryShuffleSize"
+ "XPC %!u(MISSING): Enqueuing message %!l(MISSING)d"
+ "XPC %!u(MISSING): Reading message %!l(MISSING)d"
+ "accessibilityDescription"
+ "accessibilityDescription"
+ "cache"
+ "data unavaliable"
+ "gallery"
+ "list"
+ "localIdentifierWithUUID:"
+ "other"
+ "shuffle"
+ "type"
- "    INSERT INTO stored_layout(\n        photo_id,\n        time_position,\n        base_image,\n        mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height\n    )\n    VALUES\n        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
- "    INSERT INTO stored_photo(\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        version\n    )\n    VALUES\n        (?, ?, ?, ?, ?)"
- "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        base_image,\n        mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        version\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    WHERE\n        photo_id not in(SELECT photo_id FROM tracked_gallery_photos UNION SELECT photo_id FROM tracked_shuffle_photos UNION SELECT photo_id FROM tracked_album_photos);"
- "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        base_image,\n        mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        version\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    WHERE \n        photo_id IN ("
- "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        base_image,\n        mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        version,\n        day\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    NATURAL JOIN tracked_album_photos\n    NATURAL JOIN tracked_album\n    WHERE\n        album_id = ?\n        "
- "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        base_image,\n        mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        version,\n        day\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    NATURAL JOIN tracked_album_photos\n    NATURAL JOIN tracked_album\n    WHERE\n        album_id = ?\n        AND day = ?\n        "
- "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        base_image,\n        mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        version,\n        day\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    NATURAL JOIN tracked_gallery_photos\n    NATURAL JOIN tracked_gallery\n    WHERE\n        gallery_id = ?\n        "
- "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        base_image,\n        mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        version,\n        day\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    NATURAL JOIN tracked_gallery_photos\n    NATURAL JOIN tracked_gallery\n    WHERE\n        gallery_id = ?\n        AND day = ? \n        "
- "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        base_image,\n        mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        version,\n        day\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    NATURAL JOIN tracked_shuffle_photos\n    NATURAL JOIN tracked_shuffle\n    WHERE\n        shuffle_id = ?\n        "
- "    SELECT\n        photo_id,\n        modification_date,\n        parallax_scale,\n        preferred_layout,\n        time_position,\n        base_image,\n        mask_image,\n        background_z_order,\n        foreground_z_order,\n        time_element_z_order,\n        image_aot_brightness,\n        user_edited,\n        original_crop_x,\n        original_crop_y,\n        original_crop_width,\n        original_crop_height,\n        time_rect_x,\n        time_rect_y,\n        time_rect_width,\n        time_rect_height,\n        version,\n        day\n    FROM\n        stored_photo\n    NATURAL JOIN stored_layout\n    NATURAL JOIN tracked_shuffle_photos\n    NATURAL JOIN tracked_shuffle\n    WHERE\n        shuffle_id = ?\n        AND day = ?\n        "
- ".cxx_destruct"
- "Attempting migration to version %!l(MISSING)d"
- "Caught Error: %!@(MISSING)"
- "Could not find preferred layout in StoredPhoto"
- "Message(operation: "
- "PhotoProcessResult(baseURL: "
- "PhotosFace.PhotoProcessResult"
- "PhotosFace/StoredPhoto.swift"
- "Picking %!l(MISSING)d from array of size %!l(MISSING)d, using first %!l(MISSING)d elements"
- "T@\"NSString\",N,R"
- "XPC %!u(MISSING): Enqueuing message %!l(MISSING)d)"
- "XPC %!u(MISSING): Reading message %!l(MISSING)d)"
- "_TtC10PhotosFace18PhotoProcessResult"
- "add_photo_version"
- "array"
- "baseURL"
- "begin"
- "commit"
- "content"
- "dealloc"
- "inMemory"
- "init"
- "init()"
- "metadata"
- "name"
- "onDisk"
- "processPhotosWithLocalIdentifiers:completionHandler:"
- "processPhotosWithLocalIdentifiers:fileDestination:completionHandler:"
- "rollback"
- "setBackgroundZorder:"
- "setBaseImageName:"
- "setForegroundZorder:"
- "setImageAOTBrightness:"
- "setLayouts:"
- "setLocalIdentifier:"
- "setMaskImageName:"
- "setModificationDate:"
- "setOriginalCrop:"
- "setParallaxScale:"
- "setPreferredLayout:"
- "setTimeElementZorder:"
- "setTimePosition:"
- "setTimeRect:"
- "setUserEdited:"
- "storageOption"
- "v16@0:8"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v40@0:8@\"NSArray\"16@\"NSURL\"24@?<v@?@\"NSArray\"@\"NSError\">32"

```
