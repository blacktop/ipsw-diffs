## HomeFeedbackDiagnosticExtension

> `FileSystem/private/var/staged_system_apps/Home.app/PlugIns/HomeFeedbackDiagnosticExtension.appex/Localizable.loctable`

```diff

-en.DEGroupDescription = "Camera clip videos and metadata for caption feedback"
 en.HFDEClipDetailsDescription = "Camera clip metadata for all clips"
 en.HFDEClipDetailsDisplayName = "Clips Details"
 en.HFDEClipVideoDescription = "Camera clip video"
 en.HFDEClipVideoDisplayName = "Clip %d Video"
 en.HFDEClipsDescription = "Camera clip videos"
 en.HFDEClipsDisplayName = "Clips"
-en.HFDEGroupClipsFolderDescription = "1 File, 1 Folder with clips"
+en.HFDEFileFolderCountDescription.Files.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.HFDEFileFolderCountDescription.Files.NSStringFormatValueTypeKey = "lld"
+en.HFDEFileFolderCountDescription.Files.one = "%lld file"
+en.HFDEFileFolderCountDescription.Files.other = "%lld files"
+en.HFDEFileFolderCountDescription.Folders.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.HFDEFileFolderCountDescription.Folders.NSStringFormatValueTypeKey = "lld"
+en.HFDEFileFolderCountDescription.Folders.one = "%lld folder"
+en.HFDEFileFolderCountDescription.Folders.other = "%lld folders"
+en.HFDEFileFolderCountDescription.NSStringLocalizedFormatKey = "%1$#@Files@, %2$#@Folders@"
 en.HFDEGroupDisplayName = "Home Clip Diagnostics"
-en.HFDEGroupFolderDescription = "1 File"
 en.HFDEGroupNotificationFolderDescription = "Notification details and thumbnail"
-en.HFDEGroupThumbnailsFolderDescription = "1 File, 1 Folder with thumbnails"
 en.HFDENotificationDetailsDescription = "Camera notification metadata"
 en.HFDENotificationDetailsDisplayName = "Notification Details"
 en.HFDENotificationThumbnailDescription = "Clip thumbnail from the camera notification"

```
