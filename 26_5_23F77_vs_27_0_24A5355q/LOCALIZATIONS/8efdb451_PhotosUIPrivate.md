## PhotosUIPrivate

> `FileSystem/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/AppIntents.loctable`

```diff

 en.APPLY_FILTER_INTENT_NAME = "Apply Filter"
 en.APPLY_FILTER_INTENT_PARAMETER_SUMMARY ${effect} = "Apply the ${effect} filter"
 en.APPLY_FILTER_INTENT_STYLE_FALLBACK_RESPONSE_DIALOG = "I applied a Photographic Style"
-en.COPY_EDITS_INTENT_ASSET_PARAMETER_DESCRIPTION = "The photo to copy edits from"
-en.COPY_EDITS_INTENT_ASSET_PARAMETER_TITLE = "Photo"
-en.COPY_EDITS_INTENT_DESCRIPTION = "Copies edits of the specified photo."
-en.COPY_EDITS_INTENT_PARAMETER_SUMMARY ${asset} = "Copy edits from ${asset}"
-en.COPY_EDITS_INTENT_TITLE = "Copy Edits"
+en.COPY_PASTE_EDITS_INTENT_DESCRIPTION = "Copies edits between the specified source and destination photos."
+en.COPY_PASTE_EDITS_INTENT_DESTINATION_ASSETS_PARAMETER_DESCRIPTION = "The photos to paste edits to"
+en.COPY_PASTE_EDITS_INTENT_DESTINATION_ASSETS_PARAMETER_TITLE = "Destination Photos"
+en.COPY_PASTE_EDITS_INTENT_PARAMETER_SUMMARY ${sourceAsset} ${destinationAssets} = "Copy edits from ${sourceAsset} and paste to ${destinationAssets}"
+en.COPY_PASTE_EDITS_INTENT_SOURCE_ASSET_PARAMETER_DESCRIPTION = "The photo to copy edits from"
+en.COPY_PASTE_EDITS_INTENT_SOURCE_ASSET_PARAMETER_TITLE = "Source Photo"
+en.COPY_PASTE_EDITS_INTENT_TITLE = "Copy and Paste Edits"
 en.CROP_ACTION_DESCRIPTION = "Opens the photo to Crop."
 en.CROP_ACTION_NAME = "Crop"
 en.ENABLE_DEPTH_INTENT_DESCRIPTION = "Enables or disables Portrait mode for the photo."

 en.ENHANCE_INTENT_ASSETS_PARAMETER_TITLE = "Photos"
 en.ENHANCE_INTENT_DESCRIPTION = "Enables or disables auto-enhancement of the specified photos."
 en.ENHANCE_INTENT_PARAMETER_SUMMARY ${assets} ${enabled} = "Turn auto enhance ${enabled} for ${assets}"
-en.ENHANCE_INTENT_TITLE = "Auto Enhance"
+en.ENHANCE_INTENT_TITLE = "Auto Enhance Photo"
 en.MARKUP_ACTION_DESCRIPTION = "Opens the photo to Markup."
 en.MARKUP_ACTION_NAME = "Markup"
-en.PASTE_EDITS_INTENT_ASSETS_PARAMETER_DESCRIPTION = "The photos to paste edits to"
-en.PASTE_EDITS_INTENT_ASSETS_PARAMETER_TITLE = "Photos"
-en.PASTE_EDITS_INTENT_DESCRIPTION = "Pastes edits to the specified photos."
-en.PASTE_EDITS_INTENT_PARAMETER_SUMMARY ${assets} = "Paste edits to ${assets}"
-en.PASTE_EDITS_INTENT_TITLE = "Paste Edits"
 en.ROTATE_INTENT_ASSETS_PARAMETER_DESCRIPTION = "The photos to rotate"
 en.ROTATE_INTENT_ASSETS_PARAMETER_TITLE = "Photos"
 en.ROTATE_INTENT_CLOCKWISE_PARAMETER_DESCRIPTION = "The direction to rotate"

```
