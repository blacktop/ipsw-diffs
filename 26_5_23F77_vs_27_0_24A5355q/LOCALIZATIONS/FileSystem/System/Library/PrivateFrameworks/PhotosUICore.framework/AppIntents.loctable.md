## PhotosUICore

> `FileSystem/System/Library/PrivateFrameworks/PhotosUICore.framework/AppIntents.loctable`

```diff

 en.DESTINATION_ANIMATED = "Animated"
 en.DESTINATION_ANIMATED_SYNONYM_GIF = "GIF"
 en.DESTINATION_ANIMATED_SYNONYM_MEME = "Meme"
+en.DESTINATION_CAPTURED_BY_ME = "Captured by Me"
 en.DESTINATION_CINEMATIC = "Cinematic"
 en.DESTINATION_DUPLICATES = "Duplicates"
 en.DESTINATION_ENTITY_NAME = "Destination"

 en.EDIT_ASSET_INTENT_ASSET_PARAMETER_TITLE = "Photo"
 en.EDIT_ASSET_INTENT_DESCRIPTION = "Opens the specified photo to Edit."
 en.EDIT_ASSET_INTENT_TITLE = "Edit Photo"
+en.ENTITY_COLLECTION_SEARCH_INTENT_CRITERIA_PARAMETER_TITLE = "Criteria"
+en.ENTITY_COLLECTION_SEARCH_INTENT_TITLE = "Present Search Results"
 en.ERROR_AUTO_STRAIGHTEN_FAILED_PHOTO = "That photo can't be straightened automatically, but you can edit it here."
 en.ERROR_AUTO_STRAIGHTEN_FAILED_VIDEO = "That video can't be straightened automatically, but you can edit it here."
 en.ERROR_CANNOT_FILTER_STYLED_ITEMS = "Sorry, I can’t apply filters to items captured with Photographic Style."

 en.SHAREPLAY_INTENT_ASSETS_PARAMETER_TITLE = "Photo"
 en.SHAREPLAY_INTENT_DESCRIPTION = "Starts a SharePlay session."
 en.SHAREPLAY_INTENT_TITLE = "Start SharePlay"
-en.SHAREPLAY_PARAMETER_SUMMARY = "Start a SharePlay session with ${asset}"
+en.SHAREPLAY_PARAMETER_SUMMARY ${asset} = "Start a SharePlay session with ${asset}"
 en.SPATIAL_PRESENTATION_INTENT_ASSETS_PARAMETER_DESCRIPTION = "The photo to modify"
 en.SPATIAL_PRESENTATION_INTENT_ASSETS_PARAMETER_TITLE = "Photo"
 en.SPATIAL_PRESENTATION_INTENT_DESCRIPTION = "Enables or disables spatial mode for the specified photo or video."
 en.SPATIAL_PRESENTATION_INTENT_PARAMETER_SUMMARY ${asset} ${prefersSpatialPresentation} = "Open ${asset} with spatial mode ${prefersSpatialPresentation}"
 en.SPATIAL_PRESENTATION_INTENT_TITLE = "Spatial Mode"
+en.SPATIAL_SCENE_INTENT_ASSET_PARAMETER_DESCRIPTION = "The photo to modify"
+en.SPATIAL_SCENE_INTENT_ASSET_PARAMETER_TITLE = "Photo"
+en.SPATIAL_SCENE_INTENT_DESCRIPTION = "Enables or disables spatial scene for the specified photo."
+en.SPATIAL_SCENE_INTENT_PARAMETER_SUMMARY ${asset} ${prefersSpatialScene} = "Open ${asset} with spatial scene ${prefersSpatialScene}"
+en.SPATIAL_SCENE_INTENT_TITLE = "Spatial Scene"

```
