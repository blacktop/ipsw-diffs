## PhotosUIPrivate

> `FileSystem/System/Library/PrivateFrameworks/PhotosUIPrivate.framework/AppIntents.loctable`

```diff

 en.COPY_PASTE_EDITS_INTENT_DESTINATION_ASSETS_PARAMETER_DESCRIPTION = "The photos to paste edits to"
 en.COPY_PASTE_EDITS_INTENT_DESTINATION_ASSETS_PARAMETER_TITLE = "Destination Photos"
 en.COPY_PASTE_EDITS_INTENT_PARAMETER_SUMMARY ${sourceAsset} ${destinationAssets} = "Copy edits from ${sourceAsset} and paste to ${destinationAssets}"
+en.COPY_PASTE_EDITS_INTENT_PROGRESS_DESCRIPTION = "Pasting…"
 en.COPY_PASTE_EDITS_INTENT_SOURCE_ASSET_PARAMETER_DESCRIPTION = "The photo to copy edits from"
 en.COPY_PASTE_EDITS_INTENT_SOURCE_ASSET_PARAMETER_TITLE = "Source Photo"
 en.COPY_PASTE_EDITS_INTENT_TITLE = "Copy and Paste Edits"

 en.ENHANCE_INTENT_ASSETS_PARAMETER_TITLE = "Photos"
 en.ENHANCE_INTENT_DESCRIPTION = "Enables or disables auto-enhancement of the specified photos."
 en.ENHANCE_INTENT_PARAMETER_SUMMARY ${assets} ${enabled} = "Turn auto enhance ${enabled} for ${assets}"
+en.ENHANCE_INTENT_PROGRESS_DESCRIPTION_DISABLE = "Removing enhancements…"
+en.ENHANCE_INTENT_PROGRESS_DESCRIPTION_ENABLE = "Enhancing…"
 en.ENHANCE_INTENT_TITLE = "Auto Enhance Photo"
 en.MARKUP_INTENT_ASSET_PARAMETER_DESCRIPTION = "The photo to mark up"
 en.MARKUP_INTENT_ASSET_PARAMETER_TITLE = "Photo"

 en.MARKUP_INTENT_TITLE = "Markup"
 en.ROTATE_INTENT_ASSETS_PARAMETER_DESCRIPTION = "The photos to rotate"
 en.ROTATE_INTENT_ASSETS_PARAMETER_TITLE = "Photos"
-en.ROTATE_INTENT_CLOCKWISE_PARAMETER_DESCRIPTION = "The direction to rotate"
-en.ROTATE_INTENT_CLOCKWISE_PARAMETER_TITLE = "Clockwise"
 en.ROTATE_INTENT_DESCRIPTION = "Rotates the photos in the specified direction."
 en.ROTATE_INTENT_DIRECTION_CLOCKWISE = "Clockwise"
 en.ROTATE_INTENT_DIRECTION_CLOCKWISE_SYNONYM_RIGHT = "Right"
 en.ROTATE_INTENT_DIRECTION_COUNTER_CLOCKWISE = "Counterclockwise"
 en.ROTATE_INTENT_DIRECTION_COUNTER_CLOCKWISE_SYNONYM_LEFT = "Left"
-en.ROTATE_INTENT_PARAMETER_SUMMARY ${assets} ${clockwise} = "Rotate ${assets} ${clockwise}"
+en.ROTATE_INTENT_DIRECTION_NAME = "Direction"
+en.ROTATE_INTENT_DIRECTION_PARAMETER_DESCRIPTION = "The direction to rotate"
+en.ROTATE_INTENT_DIRECTION_PARAMETER_TITLE = "Direction"
+en.ROTATE_INTENT_PARAMETER_SUMMARY ${assets} ${direction} = "Rotate ${assets} ${direction}"
+en.ROTATE_INTENT_PROGRESS_DESCRIPTION = "Rotating…"
 en.ROTATE_INTENT_TITLE = "Rotate"
 en.SET_APERTURE_INTENT_ASSET_PARAMETER_DESCRIPTION = "The photo to set aperture to"
 en.SET_APERTURE_INTENT_ASSET_PARAMETER_TITLE = "Photo"

```
