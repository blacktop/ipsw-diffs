## com.apple.WebKit.WebContent.Development

> Group: ⬆️ Updated

```diff

 (deny default)
 
 (deny darwin-notification-post)
+(allow darwin-notification-post
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow darwin-notification-post
 	(require-any
 		(notification-name "AppleCarPlayPreferredContentSizeCategoryChangedNotification")

 	)
 )
 
-(deny dynamic-code-generation)
-(allow dynamic-code-generation)
-(deny dynamic-code-generation
-	(require-any
-		(signing-identifier "com.apple.WebKit.WebContent.CaptivePortal")
-		(signing-identifier "com.apple.WebKit.WebContent.EnhancedSecurity")
-	)
-)
-
 (deny file-clone)
 
 (allow file-issue-extension

 (deny file-link)
 
 (deny file-map-executable)
+(allow file-map-executable
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow file-map-executable
 	(require-any
 		(extension "com.apple.sandbox.executable")

 
 (allow file-read*
 	(require-all
-		(require-not (require-any
-			(literal "${HOME}/Library/Preferences/com.apple.AppSupport.plist")
-			(literal "${HOME}/Library/Preferences/com.apple.WebKit.WebContent.plist")
-		))
-		(require-not (literal "${HOME}/Library/Preferences/com.apple.CFNetwork.plist"))
+		(extension "com.apple.assets.read")
 		(require-any
-			(literal "${HOME}/Library/Caches/DateFormats.plist")
-			(require-all
-				(require-not (literal "${HOME}/Library/Preferences/com.apple.mobilemail.plist"))
-				(require-any
-					(literal "${HOME}/Library/Caches/com.apple.itunesstored/url-resolution.plist")
-					(literal "${HOME}/Library/Preferences/com.apple.avfoundation.videoperformancehud.plist")
-					(literal "${HOME}/Library/Preferences/com.apple.security.plist")
-					(literal "/dev/random")
-					(literal "/dev/urandom")
-					(literal "/private/etc/fstab")
-					(literal "/private/etc/hosts")
-					(literal "/private/etc/passwd")
-					(literal "/private/etc/services")
-					(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
-					(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
-					(literal "/private/var/preferences/com.apple.networkd.plist")
-					(require-all
-						(extension "com.apple.assets.read")
-						(require-any
-							(literal "${HOME}/Library/Preferences/com.apple.security.plist")
-							(subpath "${HOME}/Library/Assets")
-							(subpath "/private/var/MobileAsset")
-						)
-					)
-					(require-all
-						(extension "com.apple.sandbox.container")
-						(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
-					)
-					(require-any
-						(literal "${HOME}/Library/Preferences/com.apple.AdLib.plist.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.EmojiPreferences.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.InputModePreferences.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.LaunchServices.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.MobileAsset.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.Preferences.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.SpeakSelection.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.VoiceOverTouch.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.WebFoundation.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.audio.virtualaudio.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.avfoundation.frecents.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.da.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.indigo.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.keyboard.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.lookup.shared.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.mobileipod.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.voiceservices.logging.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.voiceservices.plist")
-					)
-					(require-any
-						(literal "${HOME}/Library/Preferences/com.apple.avfoundation.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.coreaudio.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.coremedia.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.corevideo.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
-						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
-						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
-					)
-					(require-any
-						(literal "/dev/null")
-						(literal "/dev/zero")
-					)
-					(require-any
-						(literal "/private/etc/group")
-						(literal "/private/etc/protocols")
-					)
-					(require-any
-						(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
-						(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
-						(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
-					)
-					(require-any
-						(subpath "${HOME}/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice")
-						(subpath "${HOME}/Library/VoiceServices/Assets")
-					)
-					(require-any
-						(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
-						(subpath "/private/var/db/datadetectors/sys")
-					)
-					(subpath "${HOME}/Library/Caches/com.apple.keyboards")
-					(subpath "/")
-					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
-				)
-			)
-			(require-any
-				(literal "${HOME}/Library/Preferences/com.apple.Metal.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.coreanimation.plist")
-			)
-			(require-any
-				(literal "${HOME}/Library/Preferences/com.apple.UIKit.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.WebUI.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.airplay.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.avkit.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.iokit.IOMobileGraphicsFamily.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.mt.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.opengl.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.preferences.sounds.plist")
-			)
-			(require-any
-				(subpath "${HOME}/Library/Dictionaries")
-				(subpath "/Library/Dictionaries")
-			)
-			(subpath "${HOME}/Library/Fonts")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache")
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
 		)
 	)
 )

 		(extension "com.apple.sharing.airdrop.readonly")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences.plist")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences_m.plist")
+		(literal "${HOME}/Library/Caches/DateFormats.plist")
+		(literal "${HOME}/Library/Caches/com.apple.itunesstored/url-resolution.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.Accessibility.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.AdLib.plist.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.EmojiPreferences.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.InputModePreferences.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.LaunchServices.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.Metal.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.MobileAsset.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.Preferences.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.SpeakSelection.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.UIKit.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.VoiceOverTouch.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.WebFoundation.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.WebUI.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.airplay.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.audio.virtualaudio.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.avfoundation.frecents.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.avfoundation.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.avfoundation.videoperformancehud.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.avkit.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.coreanimation.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.coreaudio.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.coremedia.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.corevideo.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.da.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.indigo.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.iokit.IOMobileGraphicsFamily.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.keyboard.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.lookup.shared.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.mediaaccessibility.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.mediaaccessibility.public.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.mobileipod.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.mt.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.opengl.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.preferences.sounds.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.security.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.voiceservices.logging.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.voiceservices.plist")
+		(literal "/dev/null")
+		(literal "/dev/random")
+		(literal "/dev/urandom")
+		(literal "/dev/zero")
+		(literal "/private/etc/fstab")
+		(literal "/private/etc/group")
+		(literal "/private/etc/hosts")
+		(literal "/private/etc/passwd")
+		(literal "/private/etc/protocols")
+		(literal "/private/etc/services")
 		(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")
+		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
+		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
+		(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
 		(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
+		(subpath "${HOME}/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice")
+		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
+		(subpath "${HOME}/Library/Dictionaries")
+		(subpath "${HOME}/Library/Fonts")
+		(subpath "${HOME}/Library/VoiceServices/Assets")
+		(subpath "/")
+		(subpath "/Library/Dictionaries")
 		(subpath "/Library/RegionFeatures")
 		(subpath "/System/Cryptexes/App")
 		(subpath "/System/Cryptexes/OS")
 		(subpath "/System/Library")
 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
+		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
+		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
+		(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
+		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
+		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
+		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache")
+		(subpath "/private/var/db/datadetectors/sys")
 		(subpath "/private/var/db/timezone")
 		(subpath "/private/var/preferences/Logging")
 		(subpath "/usr/lib")

 
 (allow file-read-data
 	(require-all
-		(require-not (require-any
-			(literal "${HOME}/Library/Preferences/com.apple.AppSupport.plist")
-			(literal "${HOME}/Library/Preferences/com.apple.WebKit.WebContent.plist")
-		))
-		(require-not (literal "${HOME}/Library/Preferences/com.apple.CFNetwork.plist"))
+		(extension "com.apple.assets.read")
 		(require-any
-			(literal "${HOME}/Library/Caches/DateFormats.plist")
-			(require-all
-				(require-not (literal "${HOME}/Library/Preferences/com.apple.mobilemail.plist"))
-				(require-any
-					(literal "${HOME}/Library/Caches/com.apple.itunesstored/url-resolution.plist")
-					(literal "${HOME}/Library/Preferences/com.apple.avfoundation.videoperformancehud.plist")
-					(literal "${HOME}/Library/Preferences/com.apple.security.plist")
-					(literal "/dev/random")
-					(literal "/dev/urandom")
-					(literal "/private/etc/fstab")
-					(literal "/private/etc/hosts")
-					(literal "/private/etc/passwd")
-					(literal "/private/etc/services")
-					(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
-					(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
-					(literal "/private/var/preferences/com.apple.networkd.plist")
-					(require-all
-						(extension "com.apple.assets.read")
-						(require-any
-							(literal "${HOME}/Library/Preferences/com.apple.security.plist")
-							(subpath "${HOME}/Library/Assets")
-							(subpath "/private/var/MobileAsset")
-						)
-					)
-					(require-all
-						(extension "com.apple.sandbox.container")
-						(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
-					)
-					(require-any
-						(literal "${HOME}/Library/Preferences/com.apple.AdLib.plist.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.EmojiPreferences.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.InputModePreferences.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.LaunchServices.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.MobileAsset.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.Preferences.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.SpeakSelection.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.VoiceOverTouch.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.WebFoundation.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.audio.virtualaudio.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.avfoundation.frecents.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.da.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.indigo.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.keyboard.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.lookup.shared.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.mobileipod.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.voiceservices.logging.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.voiceservices.plist")
-					)
-					(require-any
-						(literal "${HOME}/Library/Preferences/com.apple.avfoundation.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.coreaudio.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.coremedia.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.corevideo.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
-						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
-						(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
-					)
-					(require-any
-						(literal "/dev/null")
-						(literal "/dev/zero")
-					)
-					(require-any
-						(literal "/private/etc/group")
-						(literal "/private/etc/protocols")
-					)
-					(require-any
-						(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
-						(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
-						(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
-					)
-					(require-any
-						(subpath "${HOME}/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice")
-						(subpath "${HOME}/Library/VoiceServices/Assets")
-					)
-					(require-any
-						(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
-						(subpath "/private/var/db/datadetectors/sys")
-					)
-					(subpath "${HOME}/Library/Caches/com.apple.keyboards")
-					(subpath "/")
-					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
-				)
-			)
-			(require-any
-				(literal "${HOME}/Library/Preferences/com.apple.Metal.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.coreanimation.plist")
-			)
-			(require-any
-				(literal "${HOME}/Library/Preferences/com.apple.UIKit.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.WebUI.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.airplay.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.avkit.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.iokit.IOMobileGraphicsFamily.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.mt.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.opengl.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.preferences.sounds.plist")
-			)
-			(require-any
-				(subpath "${HOME}/Library/Dictionaries")
-				(subpath "/Library/Dictionaries")
-			)
-			(subpath "${HOME}/Library/Fonts")
-			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache")
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
 		)
 	)
 )

 		(extension "com.apple.sharing.airdrop.readonly")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences.plist")
 		(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences_m.plist")
+		(literal "${HOME}/Library/Caches/DateFormats.plist")
+		(literal "${HOME}/Library/Caches/com.apple.itunesstored/url-resolution.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.Accessibility.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.AdLib.plist.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.EmojiPreferences.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.InputModePreferences.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.LaunchServices.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.Metal.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.MobileAsset.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.Preferences.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.SpeakSelection.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.UIKit.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.VoiceOverTouch.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.WebFoundation.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.WebUI.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.airplay.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.audio.virtualaudio.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.avfoundation.frecents.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.avfoundation.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.avfoundation.videoperformancehud.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.avkit.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.coreanimation.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.coreaudio.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.coremedia.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.corevideo.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.da.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.indigo.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.iokit.IOMobileGraphicsFamily.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.keyboard.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.lookup.shared.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.mediaaccessibility.plist")
 		(literal "${HOME}/Library/Preferences/com.apple.mediaaccessibility.public.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.mobileipod.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.mt.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.opengl.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.preferences.sounds.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.security.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.voiceservices.logging.plist")
+		(literal "${HOME}/Library/Preferences/com.apple.voiceservices.plist")
+		(literal "/dev/null")
+		(literal "/dev/random")
+		(literal "/dev/urandom")
+		(literal "/dev/zero")
+		(literal "/private/etc/fstab")
+		(literal "/private/etc/group")
+		(literal "/private/etc/hosts")
+		(literal "/private/etc/passwd")
+		(literal "/private/etc/protocols")
+		(literal "/private/etc/services")
 		(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")
+		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
+		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(literal "/usr/local/lib/log")
+		(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
+		(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
 		(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
+		(subpath "${HOME}/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice")
+		(subpath "${HOME}/Library/Caches/com.apple.keyboards")
+		(subpath "${HOME}/Library/Dictionaries")
+		(subpath "${HOME}/Library/Fonts")
+		(subpath "${HOME}/Library/VoiceServices/Assets")
+		(subpath "/")
+		(subpath "/Library/Dictionaries")
 		(subpath "/Library/RegionFeatures")
 		(subpath "/System/Cryptexes/App")
 		(subpath "/System/Cryptexes/OS")
 		(subpath "/System/Library")
 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
+		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
+		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
+		(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
+		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
+		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
+		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache")
+		(subpath "/private/var/db/datadetectors/sys")
 		(subpath "/private/var/db/timezone")
 		(subpath "/private/var/preferences/Logging")
 		(subpath "/usr/lib")

 	)
 )
 
-(allow file-read-metadata
-	(require-any
-		(literal "${HOME}/Library/Caches/powerlog.launchd")
-		(literal "${HOME}/Library/Preferences")
-		(require-not (literal "/private/var/db/MobileIdentityData/Version.plist"))
-		(vnode-type DIRECTORY SYMLINK)
-	)
-)
-
-(allow file-read-xattr
-	(require-all
-		(require-not (xattr "com.apple.security.private.*"))
-		(require-any
-			(extension "com.apple.app-sandbox.read")
-			(extension "com.apple.app-sandbox.read-write")
-			(extension "com.apple.sandbox.executable")
-			(extension "com.apple.sharing.airdrop.readonly")
-			(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences.plist")
-			(literal "${FRONT_USER_HOME}/Library/Preferences/.GlobalPreferences_m.plist")
-			(literal "${HOME}/Library/Preferences/com.apple.mediaaccessibility.public.plist")
-			(literal "/private/var/Managed Preferences/mobile/.GlobalPreferences.plist")
-			(require-all
-				(require-not (require-any
-					(literal "${HOME}/Library/Preferences/com.apple.AppSupport.plist")
-					(literal "${HOME}/Library/Preferences/com.apple.WebKit.WebContent.plist")
-				))
-				(require-not (literal "${HOME}/Library/Preferences/com.apple.CFNetwork.plist"))
-				(require-any
-					(literal "${HOME}/Library/Caches/DateFormats.plist")
-					(require-all
-						(require-not (literal "${HOME}/Library/Preferences/com.apple.mobilemail.plist"))
-						(require-any
-							(literal "${HOME}/Library/Caches/com.apple.itunesstored/url-resolution.plist")
-							(literal "${HOME}/Library/Preferences/com.apple.avfoundation.videoperformancehud.plist")
-							(literal "${HOME}/Library/Preferences/com.apple.security.plist")
-							(literal "/dev/random")
-							(literal "/dev/urandom")
-							(literal "/private/etc/fstab")
-							(literal "/private/etc/hosts")
-							(literal "/private/etc/passwd")
-							(literal "/private/etc/services")
-							(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
-							(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
-							(literal "/private/var/preferences/com.apple.networkd.plist")
-							(require-all
-								(extension "com.apple.assets.read")
-								(require-any
-									(literal "${HOME}/Library/Preferences/com.apple.security.plist")
-									(subpath "${HOME}/Library/Assets")
-									(subpath "/private/var/MobileAsset")
-								)
-							)
-							(require-all
-								(extension "com.apple.sandbox.container")
-								(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
-							)
-							(require-any
-								(literal "${HOME}/Library/Preferences/com.apple.AdLib.plist.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.EmojiPreferences.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.InputModePreferences.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.LaunchServices.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.MobileAsset.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.Preferences.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.SpeakSelection.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.VoiceOverTouch.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.WebFoundation.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.audio.virtualaudio.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.avfoundation.frecents.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.da.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.indigo.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.keyboard.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.lookup.shared.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.mobileipod.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.voiceservices.logging.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.voiceservices.plist")
-							)
-							(require-any
-								(literal "${HOME}/Library/Preferences/com.apple.avfoundation.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.coreaudio.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.coremedia.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.corevideo.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
-								(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
-								(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font7")
-								(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_Font8")
-							)
-							(require-any
-								(literal "/dev/null")
-								(literal "/dev/zero")
-							)
-							(require-any
-								(literal "/private/etc/group")
-								(literal "/private/etc/protocols")
-							)
-							(require-any
-								(subpath "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo")
-								(subpath "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo")
-								(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo")
-							)
-							(require-any
-								(subpath "${HOME}/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice")
-								(subpath "${HOME}/Library/VoiceServices/Assets")
-							)
-							(require-any
-								(subpath "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs")
-								(subpath "/private/var/db/datadetectors/sys")
-							)
-							(subpath "${HOME}/Library/Caches/com.apple.keyboards")
-							(subpath "/")
-							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
-						)
-					)
-					(require-any
-						(literal "${HOME}/Library/Preferences/com.apple.Metal.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.coreanimation.plist")
-					)
-					(require-any
-						(literal "${HOME}/Library/Preferences/com.apple.UIKit.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.WebUI.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.airplay.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.avkit.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.iokit.IOMobileGraphicsFamily.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.mt.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.opengl.plist")
-						(literal "${HOME}/Library/Preferences/com.apple.preferences.sounds.plist")
-					)
-					(require-any
-						(subpath "${HOME}/Library/Dictionaries")
-						(subpath "/Library/Dictionaries")
-					)
-					(subpath "${HOME}/Library/Fonts")
-					(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.lsd.iconscache")
-				)
-			)
-			(require-any
-				(literal "${HOME}/Library/Preferences/com.apple.Accessibility.plist")
-				(literal "${HOME}/Library/Preferences/com.apple.mediaaccessibility.plist")
-			)
-			(require-any
-				(subpath "/System/Cryptexes/App")
-				(subpath "/System/Cryptexes/OS")
-				(subpath "/private/preboot/Cryptexes/App")
-				(subpath "/private/preboot/Cryptexes/OS")
-			)
-			(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
-			(subpath "/Library/RegionFeatures")
-			(subpath "/System/Library")
-			(subpath "/private/var/db/timezone")
-			(subpath "/private/var/preferences/Logging")
-			(subpath "/usr/lib")
-			(subpath "/usr/share")
-		)
-	)
-)
+(allow file-read-metadata)
 
 (allow file-write*
 	(with report)
 	(extension "com.apple.app-sandbox.read-write")
 )
-(allow file-write*
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
-	)
-)
-(deny file-write*
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
-		(require-any
-			(literal "${HOME}/Library/Caches/DateFormats.plist")
-			(subpath "${HOME}/Library/Preferences")
-		)
-	)
-)
-
-(allow file-write-create
-	(with report)
-	(require-all
-		(require-not (vnode-type SYMLINK))
-		(require-not (require-any
-			(literal "${HOME}/Library/Preferences/com.apple.Accessibility.plist*")
-			(literal "${HOME}/Library/Preferences/com.apple.UIKit.plist*")
-		))
-		(require-any
-			(extension "com.apple.app-sandbox.read-write")
-			(require-all
-				(extension "com.apple.sandbox.container")
-				(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
-				(require-not (literal "${HOME}/Library/Caches/DateFormats.plist"))
-				(require-not (subpath "${HOME}/Library/Preferences"))
-			)
-		)
-	)
-)
-(allow file-write-create
-	(require-all
-		(require-not (vnode-type SYMLINK))
-		(require-not (require-any
-			(literal "${HOME}/Library/Preferences/com.apple.Accessibility.plist*")
-			(literal "${HOME}/Library/Preferences/com.apple.UIKit.plist*")
-		))
-		(require-any
-			(extension "com.apple.app-sandbox.read-write")
-			(require-all
-				(extension "com.apple.sandbox.container")
-				(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
-				(require-not (literal "${HOME}/Library/Caches/DateFormats.plist"))
-				(require-not (subpath "${HOME}/Library/Preferences"))
-			)
-		)
-	)
-)
 
 (allow file-write-data
 	(with report)
-	(require-all
-		(require-not (literal "/dev/urandom"))
-		(require-not (literal "/dev/random"))
-		(require-any
-			(extension "com.apple.app-sandbox.read-write")
-			(require-all
-				(extension "com.apple.sandbox.container")
-				(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
-				(require-not (literal "${HOME}/Library/Caches/DateFormats.plist"))
-				(require-not (subpath "${HOME}/Library/Preferences"))
-			)
-			(require-all
-				(require-any
-					(literal "/dev/null")
-					(literal "/dev/zero")
-				)
-				(require-not (literal "/dev/dtracehelper"))
-			)
-		)
-	)
+	(extension "com.apple.app-sandbox.read-write")
 )
 (allow file-write-data
-	(require-all
-		(require-not (literal "/dev/urandom"))
-		(require-not (literal "/dev/random"))
-		(require-any
-			(extension "com.apple.app-sandbox.read-write")
-			(require-all
-				(extension "com.apple.sandbox.container")
-				(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
-				(require-not (literal "${HOME}/Library/Caches/DateFormats.plist"))
-				(require-not (subpath "${HOME}/Library/Preferences"))
-			)
-			(require-all
-				(require-any
-					(literal "/dev/null")
-					(literal "/dev/zero")
-				)
-				(require-not (literal "/dev/dtracehelper"))
-			)
-		)
-	)
-)
-
-(allow file-write-xattr
 	(with report)
 	(require-all
-		(require-not (xattr "com.apple.security.private.*"))
 		(require-any
-			(extension "com.apple.app-sandbox.read-write")
-			(require-all
-				(extension "com.apple.sandbox.container")
-				(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
-				(require-not (literal "${HOME}/Library/Caches/DateFormats.plist"))
-				(require-not (subpath "${HOME}/Library/Preferences"))
-			)
-		)
-	)
-)
-(allow file-write-xattr
-	(require-all
-		(require-not (xattr "com.apple.security.private.*"))
-		(require-any
-			(extension "com.apple.app-sandbox.read-write")
-			(require-all
-				(extension "com.apple.sandbox.container")
-				(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")
-				(require-not (literal "${HOME}/Library/Caches/DateFormats.plist"))
-				(require-not (subpath "${HOME}/Library/Preferences"))
-			)
+			(literal "/dev/null")
+			(literal "/dev/zero")
 		)
+		(require-not (literal "/dev/dtracehelper"))
 	)
 )
 

 (deny fs-snapshot-mount)
 
 (deny iokit-get-properties)
+(allow iokit-get-properties
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow iokit-get-properties
 	(require-all
 		(iokit-registry-entry-class "IOMobileFramebuffer")

 )
 (allow iokit-get-properties
 	(require-all
-		(iokit-property "home-button-type")
 		(iokit-registry-entry-class "IOPlatformDevice")
+		(iokit-property "home-button-type")
 	)
 )
 (allow iokit-get-properties

 	)
 )
 
-(deny iokit-open-user-client
-	(with no-report)
-	(iokit-registry-entry-class "AppleJPEGDriverUserClient")
+(allow iokit-open-user-client
+	(with report)
+	(system-attribute developer-mode)
 )
-(deny iokit-open-user-client)
 
-(deny iokit-open-service
-	(with no-report)
+(deny iokit-open-service)
+(allow iokit-open-service
+	(with report)
+	(system-attribute developer-mode)
 )
 
 (allow mach-bootstrap

 
 (deny mach-cross-domain-lookup)
 
-(deny mach-lookup
-	(with no-report)
-	(require-all
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.SystemConfiguration.configd"))
-		(require-not (global-name "com.apple.fontservicesd"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.aggregated"))
-		(require-not (xpc-service-name "com.apple.audio.toolbox.reporting.service"))
-		(require-not (xpc-service-name "*"))
-		(require-not (global-name "com.apple.logd.events"))
-		(global-name "com.apple.logd")
-	)
-)
-(deny mach-lookup
-	(require-all
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.SystemConfiguration.configd"))
-		(require-not (global-name "com.apple.fontservicesd"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.aggregated"))
-		(require-not (xpc-service-name "com.apple.audio.toolbox.reporting.service"))
-		(require-not (xpc-service-name "*"))
-		(require-not (global-name "com.apple.logd.events"))
-		(global-name "com.apple.logd")
-	)
+(allow mach-lookup
+	(with report)
+	(system-attribute developer-mode)
 )
 
 (allow mach-register

 )
 
 (deny mach-task-special-port-get)
+(allow mach-task-special-port-get
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow mach-task-special-port-get
 	(require-any
 		(require-not (state-flag "local:WebContentProcessLaunched"))

 )
 
 (deny mach-task-special-port-set)
+(allow mach-task-special-port-set
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow mach-task-special-port-set)
 (deny mach-task-special-port-set
 	(state-flag "local:WebContentProcessLaunched")

 
 (deny necp-client-open)
 
-(allow network-outbound
-	(control-name "com.apple.flow-divert")
-)
-
 (deny nvram*)
 
 (deny process-info*)
-
-(deny process-info-codesignature
-	(with no-report)
+(allow process-info*
+	(with report)
+	(system-attribute developer-mode)
 )
 
 (deny process-info-dirtycontrol)
+(allow process-info-dirtycontrol
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow process-info-dirtycontrol
 	(target self)
 )
 
 (deny process-info-pidinfo)
+(allow process-info-pidinfo
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow process-info-pidinfo
 	(target self)
 )
 
 (deny process-info-pidfdinfo)
+(allow process-info-pidfdinfo
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow process-info-pidfdinfo
 	(target self)
 )
 
 (deny process-info-pidfileportinfo)
+(allow process-info-pidfileportinfo
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow process-info-pidfileportinfo
 	(target self)
 )
 
 (deny process-info-rusage)
+(allow process-info-rusage
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow process-info-rusage
 	(target self)
 )
 
-(allow process-info-sandbox-container)
-
 (deny process-info-setcontrol)
+(allow process-info-setcontrol
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow process-info-setcontrol
 	(target self)
 )
 
-(deny process-iopolicy-get)
-
-(deny process-iopolicy-set)
+(allow process-legacy-codesigning*
+	(with report)
+	(system-attribute developer-mode)
+)
 
 (allow process-legacy-codesigning-entitlements-blob-get)
 
 (allow process-legacy-codesigning-entitlements-der-blob-get)
 
+(allow process-legacy-codesigning-identity-get
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow process-legacy-codesigning-identity-get
 	(target self)
 )
 
 (allow process-legacy-codesigning-status-get)
 
+(allow process-legacy-codesigning-status-set
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow process-legacy-codesigning-status-set
 	(target self)
 )

 (deny socket-option-set)
 
 (deny syscall-unix)
+(allow syscall-unix
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow syscall-unix
 	(syscall-number
-		SYS___disable_threadsignal
-		SYS___mac_syscall
-		SYS_access
-		SYS_bsdthread_create
-		SYS_bsdthread_ctl
-		SYS_bsdthread_terminate
+		SYS_exit
+		SYS_read
+		SYS_write
+		SYS_open
 		SYS_close
-		SYS_close_nocancel
+		SYS_unlink
+		SYS_getuid
+		SYS_geteuid
+		SYS_access
+		SYS_dup
+		SYS_getegid
+		SYS_getgid
+		SYS_sigprocmask
+		SYS_ioctl
+		SYS_readlink
+		SYS_umask
+		SYS_msync
+		SYS_munmap
+		SYS_mprotect
+		SYS_madvise
+		SYS_fcntl
+		SYS_fsync
+		SYS_gettimeofday
+		SYS_getrusage
+		SYS_writev
+		SYS_rename
+		SYS_flock
+		SYS_sendto
+		SYS_mkdir
+		SYS_rmdir
+		SYS_pread
 		SYS_csops
 		SYS_csops_audittoken
-		SYS_dup
-		SYS_exit
-		SYS_faccessat
-		SYS_fcntl
-		SYS_fcntl_nocancel
-		SYS_fgetxattr
-		SYS_fstat64
-		SYS_fstatat64
-		SYS_fstatfs64
-		SYS_getattrlist
-		SYS_getdirentries64
-		SYS_getegid
-		SYS_getentropy
-		SYS_geteuid
-		SYS_getfsstat64
-		SYS_getrlimit
-		SYS_getrusage
-		SYS_gettid
-		SYS_gettimeofday
-		SYS_getuid
-		SYS_getxattr
-		SYS_ioctl
-		SYS_issetugid
-		SYS_kevent_id
-		SYS_kevent_qos
-		SYS_lseek
-		SYS_lstat64
-		SYS_madvise
-		SYS_map_with_linking_np
-		SYS_memorystatus_control
-		SYS_mmap
-		SYS_mprotect
-		SYS_munmap
-		SYS_open
-		SYS_open_nocancel
-		SYS_openat
-		SYS_os_fault_with_payload
 		SYS_pathconf
-		SYS_pread
-		SYS_proc_info
+		SYS_getrlimit
+		SYS_setrlimit
+		SYS_mmap
+		SYS_lseek
+		SYS_ftruncate
+		SYS_sysctl
+		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
+		SYS_getattrlist
+		SYS_fgetattrlist
+		SYS_fsetattrlist
+		SYS_getxattr
+		SYS_fgetxattr
+		SYS_fsetxattr
+		SYS_listxattr
+		SYS_shm_open
+		SYS_sem_open
+		SYS_sem_close
+		SYS_sysctlbyname
+		SYS_gettid
+		SYS_psynch_mutexwait
+		SYS_psynch_mutexdrop
 		SYS_psynch_cvbroad
-		SYS_psynch_cvclrprepost
 		SYS_psynch_cvsignal
 		SYS_psynch_cvwait
-		SYS_psynch_mutexdrop
-		SYS_psynch_mutexwait
 		SYS_psynch_rw_rdlock
-		SYS_psynch_rw_unlock
 		SYS_psynch_rw_wrlock
-		SYS_read
-		SYS_read_nocancel
-		SYS_readlink
-		SYS_shm_open
-		SYS_sigprocmask
+		SYS_psynch_rw_unlock
+		SYS_psynch_cvclrprepost
+		SYS_issetugid
+		SYS___pthread_kill
+		SYS___pthread_sigmask
+		SYS___disable_threadsignal
+		SYS___semwait_signal
+		SYS_proc_info
 		SYS_stat64
+		SYS_fstat64
+		SYS_lstat64
+		SYS_fstat64_extended
+		SYS_getdirentries64
 		SYS_statfs64
-		SYS_sysctl
-		SYS_thread_selfid
-		SYS_ulock_wait
-		SYS_ulock_wait2
-		SYS_ulock_wake
-		SYS_umask
+		SYS_fstatfs64
+		SYS_getfsstat64
+		SYS_bsdthread_create
+		SYS_bsdthread_terminate
+		SYS_kqueue
 		SYS_workq_kernreturn
+		SYS_thread_selfid
+		SYS_kevent_qos
+		SYS_kevent_id
+		SYS___mac_syscall
+		SYS_read_nocancel
 		SYS_write_nocancel
-		SYS_writev)
+		SYS_open_nocancel
+		SYS_close_nocancel
+		SYS_fcntl_nocancel
+		SYS_pread_nocancel
+		SYS_fileport_makefd
+		SYS_memorystatus_control
+		SYS_guarded_open_np
+		SYS_guarded_close_np
+		SYS_change_fdguard_np
+		SYS_getattrlistbulk
+		SYS_openat
+		SYS_openat_nocancel
+		SYS_renameat
+		SYS_faccessat
+		SYS_fstatat64
+		SYS_mkdirat
+		SYS_bsdthread_ctl
+		SYS_thread_selfusage
+		SYS_guarded_open_dprotected_np
+		SYS_guarded_pwrite_np
+		SYS_getentropy
+		SYS_ulock_wait
+		SYS_ulock_wake
+		SYS_abort_with_payload
+		SYS_os_fault_with_payload
+		SYS_kqueue_workloop_ctl
+		SYS_shared_region_map_and_slide_2_np
+		SYS_ulock_wait2
+		SYS_map_with_linking_np)
 )
 (allow syscall-unix
 	(require-all
-		(require-not (syscall-number SYS_persona))
-		(require-not (syscall-number SYS_connect))
-		(require-not (syscall-number SYS_socket))
-		(require-not (syscall-number SYS_crossarch_trap))
-		(require-not (syscall-number SYS_sigreturn))
-		(require-any
-			(require-all
-				(state-flag "ParentProcessCanEnableQuickLookStateFlag")
-				(require-any
-					(require-all
-						(state-flag "EnableQuickLookSandboxResources")
-						(syscall-number SYS_sendto)
-					)
-					(require-all
-						(syscall-number
-							SYS_exit
-							SYS_read
-							SYS_write
-							SYS_open
-							SYS_close
-							SYS_unlink
-							SYS_getuid
-							SYS_geteuid
-							SYS_access
-							SYS_dup
-							SYS_getegid
-							SYS_getgid
-							SYS_sigprocmask
-							SYS_ioctl
-							SYS_readlink
-							SYS_umask
-							SYS_msync
-							SYS_munmap
-							SYS_mprotect
-							SYS_madvise
-							SYS_fcntl
-							SYS_fsync
-							SYS_gettimeofday
-							SYS_getrusage
-							SYS_writev
-							SYS_rename
-							SYS_flock
-							SYS_mkdir
-							SYS_rmdir
-							SYS_pread
-							SYS_csops
-							SYS_csops_audittoken
-							SYS_pathconf
-							SYS_getrlimit
-							SYS_setrlimit
-							SYS_mmap
-							SYS_lseek
-							SYS_ftruncate
-							SYS_sysctl
-							SYS_open_dprotected_np
-							SYS_openat_dprotected_np
-							SYS_getattrlist
-							SYS_fgetattrlist
-							SYS_fsetattrlist
-							SYS_getxattr
-							SYS_fgetxattr
-							SYS_fsetxattr
-							SYS_listxattr
-							SYS_shm_open
-							SYS_sem_open
-							SYS_sem_close
-							SYS_sysctlbyname
-							SYS_gettid
-							SYS_psynch_mutexwait
-							SYS_psynch_mutexdrop
-							SYS_psynch_cvbroad
-							SYS_psynch_cvsignal
-							SYS_psynch_cvwait
-							SYS_psynch_rw_rdlock
-							SYS_psynch_rw_wrlock
-							SYS_psynch_rw_unlock
-							SYS_psynch_cvclrprepost
-							SYS_issetugid
-							SYS___pthread_kill
-							SYS___pthread_sigmask
-							SYS___disable_threadsignal
-							SYS___semwait_signal
-							SYS_proc_info
-							SYS_stat64
-							SYS_fstat64
-							SYS_lstat64
-							SYS_fstat64_extended
-							SYS_getdirentries64
-							SYS_statfs64
-							SYS_fstatfs64
-							SYS_getfsstat64
-							SYS_bsdthread_create
-							SYS_bsdthread_terminate
-							SYS_kqueue
-							SYS_workq_kernreturn
-							SYS_thread_selfid
-							SYS_kevent_qos
-							SYS_kevent_id
-							SYS___mac_syscall
-							SYS_read_nocancel
-							SYS_write_nocancel
-							SYS_open_nocancel
-							SYS_close_nocancel
-							SYS_fcntl_nocancel
-							SYS_pread_nocancel
-							SYS_fileport_makefd
-							SYS_memorystatus_control
-							SYS_guarded_open_np
-							SYS_guarded_close_np
-							SYS_change_fdguard_np
-							SYS_getattrlistbulk
-							SYS_openat
-							SYS_openat_nocancel
-							SYS_renameat
-							SYS_faccessat
-							SYS_fstatat64
-							SYS_mkdirat
-							SYS_bsdthread_ctl
-							SYS_thread_selfusage
-							SYS_guarded_open_dprotected_np
-							SYS_guarded_pwrite_np
-							SYS_getentropy
-							SYS_ulock_wait
-							SYS_ulock_wake
-							SYS_abort_with_payload
-							SYS_os_fault_with_payload
-							SYS_kqueue_workloop_ctl
-							SYS_shared_region_map_and_slide_2_np
-							SYS_ulock_wait2)
-						(require-not (syscall-number SYS_sendto))
-						(require-not (syscall-number SYS_unlink))
-						(require-not (syscall-number SYS_rmdir))
-						(require-not (syscall-number SYS_openat_nocancel))
-						(require-not (syscall-number SYS_thread_selfusage))
-						(require-not (syscall-number SYS_mkdirat))
-						(require-not (syscall-number SYS_pread_nocancel))
-					)
-				)
-			)
-			(require-all
-				(syscall-number
-					SYS_chdir
-					SYS_getpid
-					SYS_sigaction
-					SYS_dup2
-					SYS_kdebug_typefilter
-					SYS_kdebug_trace_string
-					SYS_kdebug_trace64
-					SYS_shared_region_check_np
-					SYS_bsdthread_register
-					SYS_workq_open
-					SYS_fsgetpath
-					SYS_persona
-					SYS_objc_bp_assist_cfg_np)
-				(require-not (state-flag "local:WebContentProcessLaunched"))
-			)
-			(syscall-number
-				SYS_exit
-				SYS_read
-				SYS_write
-				SYS_open
-				SYS_close
-				SYS_unlink
-				SYS_getuid
-				SYS_geteuid
-				SYS_access
-				SYS_dup
-				SYS_getegid
-				SYS_getgid
-				SYS_sigprocmask
-				SYS_ioctl
-				SYS_readlink
-				SYS_umask
-				SYS_msync
-				SYS_munmap
-				SYS_mprotect
-				SYS_madvise
-				SYS_fcntl
-				SYS_fsync
-				SYS_gettimeofday
-				SYS_getrusage
-				SYS_writev
-				SYS_rename
-				SYS_flock
-				SYS_mkdir
-				SYS_rmdir
-				SYS_pread
-				SYS_csops
-				SYS_csops_audittoken
-				SYS_pathconf
-				SYS_getrlimit
-				SYS_setrlimit
-				SYS_mmap
-				SYS_lseek
-				SYS_ftruncate
-				SYS_sysctl
-				SYS_open_dprotected_np
-				SYS_openat_dprotected_np
-				SYS_getattrlist
-				SYS_fgetattrlist
-				SYS_fsetattrlist
-				SYS_getxattr
-				SYS_fgetxattr
-				SYS_fsetxattr
-				SYS_listxattr
-				SYS_shm_open
-				SYS_sem_open
-				SYS_sem_close
-				SYS_sysctlbyname
-				SYS_gettid
-				SYS_psynch_mutexwait
-				SYS_psynch_mutexdrop
-				SYS_psynch_cvbroad
-				SYS_psynch_cvsignal
-				SYS_psynch_cvwait
-				SYS_psynch_rw_rdlock
-				SYS_psynch_rw_wrlock
-				SYS_psynch_rw_unlock
-				SYS_psynch_cvclrprepost
-				SYS_issetugid
-				SYS___pthread_kill
-				SYS___pthread_sigmask
-				SYS___disable_threadsignal
-				SYS___semwait_signal
-				SYS_proc_info
-				SYS_stat64
-				SYS_fstat64
-				SYS_lstat64
-				SYS_fstat64_extended
-				SYS_getdirentries64
-				SYS_statfs64
-				SYS_fstatfs64
-				SYS_getfsstat64
-				SYS_bsdthread_create
-				SYS_bsdthread_terminate
-				SYS_kqueue
-				SYS_workq_kernreturn
-				SYS_thread_selfid
-				SYS_kevent_qos
-				SYS_kevent_id
-				SYS___mac_syscall
-				SYS_read_nocancel
-				SYS_write_nocancel
-				SYS_open_nocancel
-				SYS_close_nocancel
-				SYS_fcntl_nocancel
-				SYS_pread_nocancel
-				SYS_fileport_makefd
-				SYS_memorystatus_control
-				SYS_guarded_open_np
-				SYS_guarded_close_np
-				SYS_change_fdguard_np
-				SYS_getattrlistbulk
-				SYS_openat
-				SYS_openat_nocancel
-				SYS_renameat
-				SYS_faccessat
-				SYS_fstatat64
-				SYS_mkdirat
-				SYS_bsdthread_ctl
-				SYS_thread_selfusage
-				SYS_guarded_open_dprotected_np
-				SYS_guarded_pwrite_np
-				SYS_getentropy
-				SYS_ulock_wait
-				SYS_ulock_wake
-				SYS_abort_with_payload
-				SYS_os_fault_with_payload
-				SYS_kqueue_workloop_ctl
-				SYS_shared_region_map_and_slide_2_np
-				SYS_ulock_wait2)
-			(syscall-number SYS_sendto)
-		)
+		(syscall-number SYS_kdebug_trace64 SYS_kdebug_typefilter)
+		(system-attribute developer-mode)
 	)
 )
 (allow syscall-unix
 	(require-all
-		(system-attribute developer-mode)
+		(syscall-number
+			SYS_chdir
+			SYS_getpid
+			SYS_sigaction
+			SYS_dup2
+			SYS_shared_region_check_np
+			SYS_bsdthread_register
+			SYS_workq_open
+			SYS_fsgetpath
+			SYS_persona
+			SYS_objc_bp_assist_cfg_np)
+		(require-not (state-flag "local:WebContentProcessLaunched"))
+	)
+)
+(allow syscall-unix
+	(require-all
+		(syscall-number SYS_kdebug_trace_string)
 		(require-any
-			(syscall-number SYS_kdebug_trace64)
-			(syscall-number SYS_kdebug_trace_string)
-			(syscall-number SYS_kdebug_typefilter)
+			(require-not (state-flag "local:WebContentProcessLaunched"))
+			(system-attribute developer-mode)
 		)
 	)
 )
 
 (deny syscall-mach)
 (allow syscall-mach
-	(machtrap-number
-		MSC__kernelrpc_mach_port_allocate_trap
-		MSC__kernelrpc_mach_port_construct_trap
-		MSC__kernelrpc_mach_port_deallocate_trap
-		MSC__kernelrpc_mach_port_destruct_trap
-		MSC__kernelrpc_mach_port_extract_member_trap
-		MSC__kernelrpc_mach_port_get_attributes_trap
-		MSC__kernelrpc_mach_port_guard_trap
-		MSC__kernelrpc_mach_port_insert_member_trap
-		MSC__kernelrpc_mach_port_insert_right_trap
-		MSC__kernelrpc_mach_port_mod_refs_trap
-		MSC__kernelrpc_mach_port_request_notification_trap
-		MSC__kernelrpc_mach_port_type_trap
-		MSC__kernelrpc_mach_port_unguard_trap
-		MSC__kernelrpc_mach_vm_allocate_trap
-		MSC__kernelrpc_mach_vm_deallocate_trap
-		MSC__kernelrpc_mach_vm_map_trap
-		MSC__kernelrpc_mach_vm_protect_trap
-		MSC__kernelrpc_mach_vm_purgable_control_trap
-		MSC_host_create_mach_voucher_trap
-		MSC_host_self_trap
-		MSC_iokit_user_client_trap
-		MSC_mach_generate_activity_id
-		MSC_mach_msg2_trap
-		MSC_mach_msg_trap
-		MSC_mach_reply_port
-		MSC_mach_voucher_extract_attr_recipe_trap
-		MSC_mk_timer_arm
-		MSC_mk_timer_cancel
-		MSC_mk_timer_create
-		MSC_mk_timer_destroy
-		MSC_pid_for_task
-		MSC_semaphore_signal_trap
-		MSC_semaphore_timedwait_trap
-		MSC_semaphore_wait_trap
-		MSC_swtch_pri
-		MSC_syscall_thread_switch
-		MSC_task_name_for_pid
-		MSC_thread_get_special_reply_port
-		MSC_thread_self_trap)
+	(with report)
+	(system-attribute developer-mode)
 )
 (allow syscall-mach
-	(require-all
-		(machtrap-number MSC_mach_timebase_info_trap MSC_task_self_trap)
-		(require-not (state-flag "local:WebContentProcessLaunched"))
-	)
+	(machtrap-number
+		MSC__kernelrpc_mach_vm_allocate_trap
+		MSC__kernelrpc_mach_vm_purgable_control_trap
+		MSC__kernelrpc_mach_vm_deallocate_trap
+		MSC__kernelrpc_mach_vm_protect_trap
+		MSC__kernelrpc_mach_vm_map_trap
+		MSC__kernelrpc_mach_port_allocate_trap
+		MSC__kernelrpc_mach_port_deallocate_trap
+		MSC__kernelrpc_mach_port_mod_refs_trap
+		MSC__kernelrpc_mach_port_insert_right_trap
+		MSC__kernelrpc_mach_port_insert_member_trap
+		MSC__kernelrpc_mach_port_extract_member_trap
+		MSC__kernelrpc_mach_port_construct_trap
+		MSC__kernelrpc_mach_port_destruct_trap
+		MSC_mach_reply_port
+		MSC_thread_self_trap
+		MSC_task_self_trap
+		MSC_host_self_trap
+		MSC_mach_msg_trap
+		MSC_semaphore_signal_trap
+		MSC_semaphore_wait_trap
+		MSC_semaphore_timedwait_trap
+		MSC__kernelrpc_mach_port_get_attributes_trap
+		MSC__kernelrpc_mach_port_guard_trap
+		MSC__kernelrpc_mach_port_unguard_trap
+		MSC_mach_generate_activity_id
+		MSC_task_name_for_pid
+		MSC_pid_for_task
+		MSC_mach_msg2_trap
+		MSC_thread_get_special_reply_port
+		MSC_swtch_pri
+		MSC_syscall_thread_switch
+		MSC_host_create_mach_voucher_trap
+		MSC_mach_voucher_extract_attr_recipe_trap
+		MSC__kernelrpc_mach_port_type_trap
+		MSC__kernelrpc_mach_port_request_notification_trap
+		MSC_mach_timebase_info_trap
+		MSC_mk_timer_create
+		MSC_mk_timer_destroy
+		MSC_mk_timer_arm
+		MSC_mk_timer_cancel
+		MSC_iokit_user_client_trap)
 )
 
+(deny syscall-mig)
+(allow syscall-mig
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow syscall-mig
 	(kernel-mig-routine
-		host_get_io_master
+		_mach_make_memory_entry
+		clock_get_time
 		host_get_clock_service
+		host_get_io_master
+		host_get_special_port
+		host_info
+		io_iterator_next
 		io_registry_entry_from_path
-		io_service_open_extended
-		io_server_version
 		io_registry_entry_get_property_bin_buf
-		mach_port_get_refs
-		mach_port_request_notification
+		io_registry_entry_get_property_bytes
+		io_registry_entry_get_registry_entry_id
+		io_server_version
+		io_service_open_extended
+		mach_exception_raise
+		mach_memory_entry_ownership
 		mach_port_extract_right
-		mach_port_set_attributes
 		mach_port_get_context_from_user
+		mach_port_get_refs
 		mach_port_is_connection_for_service
-		task_info_from_user
-		task_get_special_port_from_user
+		mach_port_request_notification
+		mach_port_set_attributes
+		mach_vm_copy
+		mach_vm_map_external
+		mach_vm_range_create
+		mach_vm_region
+		mach_vm_region_recurse
+		mach_voucher_attr_command
 		semaphore_create
 		semaphore_destroy
 		task_create_identity_token
+		task_get_special_port_from_user
+		task_info_from_user
+		task_restartable_ranges_register
+		task_restartable_ranges_synchronize
+		task_set_exc_guard_behavior
+		task_set_special_port
+		task_threads_from_user
 		thread_get_state_to_user
-		thread_suspend
+		thread_info
+		thread_policy
+		thread_policy_set
 		thread_resume
-		mach_vm_copy
-		mach_vm_map_external
-		mach_vm_remap_external
-		mach_vm_region_recurse
-		_mach_make_memory_entry
-		mach_memory_entry_ownership
-		mach_voucher_attr_command
-		task_restartable_ranges_synchronize)
+		thread_suspend)
 )
 (allow syscall-mig
 	(require-all
-		(require-not (kernel-mig-routine io_service_get_matching_services_bin))
-		(require-not (kernel-mig-routine io_service_get_matching_service_bin))
-		(require-any
-			(kernel-mig-routine
-				host_get_io_master
-				host_get_clock_service
-				clock_get_time
-				mach_exception_raise
-				io_iterator_next
-				io_registry_entry_from_path
-				io_registry_entry_get_property_bytes
-				io_service_open_extended
-				io_registry_entry_get_registry_entry_id
-				io_server_version
-				io_registry_entry_get_property_bin_buf
-				mach_port_get_refs
-				mach_port_request_notification
-				mach_port_extract_right
-				mach_port_set_attributes
-				mach_port_get_context_from_user
-				task_threads_from_user
-				task_info_from_user
-				task_get_special_port_from_user
-				semaphore_create
-				semaphore_destroy
-				task_set_exc_guard_behavior
-				task_create_identity_token
-				thread_get_state_to_user
-				thread_suspend
-				thread_resume
-				thread_info
-				thread_policy
-				thread_policy_set
-				mach_vm_copy
-				mach_vm_map_external
-				mach_vm_remap_external
-				mach_vm_region_recurse
-				mach_vm_region
-				_mach_make_memory_entry
-				mach_memory_entry_ownership
-				mach_voucher_attr_command
-				task_restartable_ranges_synchronize)
-			(require-all
-				(kernel-mig-routine host_get_special_port)
-				(require-not (state-flag "local:WebContentProcessLaunched"))
-			)
-			(require-all
-				(kernel-mig-routine host_info)
-				(require-not (state-flag "local:WebContentProcessLaunched"))
-			)
-			(require-all
-				(kernel-mig-routine mach_vm_range_create)
-				(require-not (state-flag "local:WebContentProcessLaunched"))
-			)
-			(require-all
-				(kernel-mig-routine task_restartable_ranges_register)
-				(require-not (state-flag "local:WebContentProcessLaunched"))
-			)
-			(require-all
-				(kernel-mig-routine task_set_special_port)
-				(require-not (state-flag "local:WebContentProcessLaunched"))
-			)
-		)
-	)
-)
-
-(allow mach-kernel-endpoint
-	(apply-message-filter
-		(deny mach-message-send)
-		(allow mach-message-send
-			(require-all
-				(kernel-mig-routine task_register_hardened_exception_handler)
-				(require-not (state-flag "local:WebContentProcessLaunched"))
-			)
-		)
-		(allow mach-message-send
-			(kernel-mig-routine thread_adopt_exception_handler)
-		)
+		(kernel-mig-routine
+			task_register_hardened_exception_handler
+			thread_adopt_exception_handler)
+		(require-not (signing-identifier "com.apple.WebKit.WebContent.CaptivePortal"))
 	)
 )
 
 (allow sysctl-read
-	(require-all
+	(with report)
+	(system-attribute developer-mode)
+)
+(allow sysctl-read
+	(require-any
+		(sysctl-name "hw.activecpu")
+		(sysctl-name "hw.availcpu")
+		(sysctl-name "hw.byteorder")
+		(sysctl-name "hw.cacheconfig")
+		(sysctl-name "hw.cachelinesize")
+		(sysctl-name "hw.cachelinesize_compat")
+		(sysctl-name "hw.cachesize")
+		(sysctl-name "hw.cpufamily")
+		(sysctl-name "hw.cpusubfamily")
+		(sysctl-name "hw.cputhreadtype")
+		(sysctl-name "hw.cputype")
+		(sysctl-name "hw.l1dcachesize")
+		(sysctl-name "hw.l1icachesize")
+		(sysctl-name "hw.l2cachesize")
+		(sysctl-name "hw.l3cachesize")
+		(sysctl-name "hw.logicalcpu")
+		(sysctl-name "hw.logicalcpu_max")
+		(sysctl-name "hw.machine")
+		(sysctl-name "hw.memsize")
+		(sysctl-name "hw.model")
+		(sysctl-name "hw.ncpu")
+		(sysctl-name "hw.nperflevels")
+		(sysctl-name "hw.optional.*")
+		(sysctl-name "hw.pagesize")
+		(sysctl-name "hw.pagesize_compat")
+		(sysctl-name "hw.perflevel*")
+		(sysctl-name "hw.physicalcpu")
+		(sysctl-name "hw.physicalcpu_max")
+		(sysctl-name "hw.physmem")
+		(sysctl-name "hw.product")
+		(sysctl-name "hw.vectorunit")
+		(sysctl-name "kern.bootargs")
+		(sysctl-name "kern.bootsessionuuid")
+		(sysctl-name "kern.boottime")
+		(sysctl-name "kern.hostname")
+		(sysctl-name "kern.hv_vmm_present")
+		(sysctl-name "kern.maxfilesperproc")
+		(sysctl-name "kern.memorystatus_level")
+		(sysctl-name "kern.osproductversion")
+		(sysctl-name "kern.osrelease")
+		(sysctl-name "kern.ostype")
+		(sysctl-name "kern.osvariant_status")
+		(sysctl-name "kern.osversion")
+		(sysctl-name "kern.secure_kernel")
+		(sysctl-name "kern.version")
+		(sysctl-name "kern.willshutdown")
+		(sysctl-name "net.routetable*")
+		(sysctl-name "sysctl.name2oid")
+		(sysctl-name "vm.footprint_suspend")
 		(sysctl-name "vm.malloc_ranges")
-		(require-not (state-flag "local:WebContentProcessLaunched"))
-	)
-)
-(allow sysctl-read
-	(require-all
-		(require-not (sysctl-name "vm.task_no_footprint_for_debug"))
-		(require-any
-			(require-all
-				(require-not (sysctl-name "hw.cpufrequency_compat"))
-				(require-not (sysctl-name "sysctl.proc_native"))
-				(sysctl-name "hw.tbfrequency_compat")
-			)
-			(require-all
-				(sysctl-name "kern.boottime")
-				(require-not (state-flag "local:WebContentProcessLaunched"))
-			)
-			(require-any
-				(sysctl-name "hw.activecpu")
-				(sysctl-name "hw.machine")
-				(sysctl-name "hw.memsize")
-				(sysctl-name "hw.ncpu")
-				(sysctl-name "kern.osproductversion")
-				(sysctl-name "kern.osvariant_status")
-				(sysctl-name "kern.secure_kernel")
-			)
-			(require-any
-				(sysctl-name "hw.availcpu")
-				(sysctl-name "hw.cputhreadtype")
-				(sysctl-name "net.routetable*")
-			)
-			(require-any
-				(sysctl-name "hw.byteorder")
-				(sysctl-name "hw.cacheconfig")
-				(sysctl-name "hw.cachelinesize_compat")
-				(sysctl-name "hw.cachesize")
-				(sysctl-name "hw.cputype")
-				(sysctl-name "hw.l1dcachesize")
-				(sysctl-name "hw.l1icachesize")
-				(sysctl-name "hw.l3cachesize")
-				(sysctl-name "hw.optional.*")
-				(sysctl-name "hw.pagesize")
-				(sysctl-name "hw.physmem")
-				(sysctl-name "hw.vectorunit")
-				(sysctl-name "kern.memorystatus_level")
-			)
-			(require-any
-				(sysctl-name "hw.cachelinesize")
-				(sysctl-name "hw.cpufamily")
-				(sysctl-name "hw.l2cachesize")
-				(sysctl-name "hw.perflevel*")
-				(sysctl-name "kern.hv_vmm_present")
-			)
-			(require-any
-				(sysctl-name "hw.logicalcpu")
-				(sysctl-name "hw.nperflevels")
-				(sysctl-name "sysctl.name2oid")
-			)
-			(require-any
-				(sysctl-name "hw.logicalcpu_max")
-				(sysctl-name "hw.model")
-				(sysctl-name "hw.physicalcpu_max")
-				(sysctl-name "hw.product")
-			)
-			(require-any
-				(sysctl-name "kern.hostname")
-				(sysctl-name "kern.ostype")
-				(sysctl-name "kern.version")
-			)
-			(require-any
-				(sysctl-name "kern.maxfilesperproc")
-				(sysctl-name "kern.osversion")
-			)
-			(sysctl-name "hw.cpusubfamily")
-			(sysctl-name "hw.pagesize_compat")
-			(sysctl-name "hw.physicalcpu")
-			(sysctl-name "kern.bootargs")
-			(sysctl-name "kern.bootsessionuuid")
-			(sysctl-name "kern.osrelease")
-			(sysctl-name "kern.willshutdown")
-			(sysctl-name "vm.footprint_suspend")
-		)
-	)
-)
-(deny sysctl-read
-	(with no-report)
-	(require-all
-		(require-not (sysctl-name "vm.task_no_footprint_for_debug"))
-		(require-any
-			(require-all
-				(require-not (sysctl-name "hw.cpufrequency_compat"))
-				(require-not (sysctl-name "sysctl.proc_native"))
-				(sysctl-name "hw.tbfrequency_compat")
-			)
-			(require-all
-				(sysctl-name "kern.boottime")
-				(require-not (state-flag "local:WebContentProcessLaunched"))
-			)
-			(require-any
-				(sysctl-name "hw.activecpu")
-				(sysctl-name "hw.machine")
-				(sysctl-name "hw.memsize")
-				(sysctl-name "hw.ncpu")
-				(sysctl-name "kern.osproductversion")
-				(sysctl-name "kern.osvariant_status")
-				(sysctl-name "kern.secure_kernel")
-			)
-			(require-any
-				(sysctl-name "hw.availcpu")
-				(sysctl-name "hw.cputhreadtype")
-				(sysctl-name "net.routetable*")
-			)
-			(require-any
-				(sysctl-name "hw.byteorder")
-				(sysctl-name "hw.cacheconfig")
-				(sysctl-name "hw.cachelinesize_compat")
-				(sysctl-name "hw.cachesize")
-				(sysctl-name "hw.cputype")
-				(sysctl-name "hw.l1dcachesize")
-				(sysctl-name "hw.l1icachesize")
-				(sysctl-name "hw.l3cachesize")
-				(sysctl-name "hw.optional.*")
-				(sysctl-name "hw.pagesize")
-				(sysctl-name "hw.physmem")
-				(sysctl-name "hw.vectorunit")
-				(sysctl-name "kern.memorystatus_level")
-			)
-			(require-any
-				(sysctl-name "hw.cachelinesize")
-				(sysctl-name "hw.cpufamily")
-				(sysctl-name "hw.l2cachesize")
-				(sysctl-name "hw.perflevel*")
-				(sysctl-name "kern.hv_vmm_present")
-			)
-			(require-any
-				(sysctl-name "hw.logicalcpu")
-				(sysctl-name "hw.nperflevels")
-				(sysctl-name "sysctl.name2oid")
-			)
-			(require-any
-				(sysctl-name "hw.logicalcpu_max")
-				(sysctl-name "hw.model")
-				(sysctl-name "hw.physicalcpu_max")
-				(sysctl-name "hw.product")
-			)
-			(require-any
-				(sysctl-name "kern.hostname")
-				(sysctl-name "kern.ostype")
-				(sysctl-name "kern.version")
-			)
-			(require-any
-				(sysctl-name "kern.maxfilesperproc")
-				(sysctl-name "kern.osversion")
-			)
-			(sysctl-name "hw.cpusubfamily")
-			(sysctl-name "hw.pagesize_compat")
-			(sysctl-name "hw.physicalcpu")
-			(sysctl-name "kern.bootargs")
-			(sysctl-name "kern.bootsessionuuid")
-			(sysctl-name "kern.osrelease")
-			(sysctl-name "kern.willshutdown")
-			(sysctl-name "vm.footprint_suspend")
-		)
-	)
-)
-(deny sysctl-read
-	(require-all
-		(require-not (sysctl-name "vm.task_no_footprint_for_debug"))
-		(require-any
-			(require-all
-				(require-not (sysctl-name "hw.cpufrequency_compat"))
-				(require-not (sysctl-name "sysctl.proc_native"))
-				(sysctl-name "hw.tbfrequency_compat")
-			)
-			(require-all
-				(sysctl-name "kern.boottime")
-				(require-not (state-flag "local:WebContentProcessLaunched"))
-			)
-			(require-any
-				(sysctl-name "hw.activecpu")
-				(sysctl-name "hw.machine")
-				(sysctl-name "hw.memsize")
-				(sysctl-name "hw.ncpu")
-				(sysctl-name "kern.osproductversion")
-				(sysctl-name "kern.osvariant_status")
-				(sysctl-name "kern.secure_kernel")
-			)
-			(require-any
-				(sysctl-name "hw.availcpu")
-				(sysctl-name "hw.cputhreadtype")
-				(sysctl-name "net.routetable*")
-			)
-			(require-any
-				(sysctl-name "hw.byteorder")
-				(sysctl-name "hw.cacheconfig")
-				(sysctl-name "hw.cachelinesize_compat")
-				(sysctl-name "hw.cachesize")
-				(sysctl-name "hw.cputype")
-				(sysctl-name "hw.l1dcachesize")
-				(sysctl-name "hw.l1icachesize")
-				(sysctl-name "hw.l3cachesize")
-				(sysctl-name "hw.optional.*")
-				(sysctl-name "hw.pagesize")
-				(sysctl-name "hw.physmem")
-				(sysctl-name "hw.vectorunit")
-				(sysctl-name "kern.memorystatus_level")
-			)
-			(require-any
-				(sysctl-name "hw.cachelinesize")
-				(sysctl-name "hw.cpufamily")
-				(sysctl-name "hw.l2cachesize")
-				(sysctl-name "hw.perflevel*")
-				(sysctl-name "kern.hv_vmm_present")
-			)
-			(require-any
-				(sysctl-name "hw.logicalcpu")
-				(sysctl-name "hw.nperflevels")
-				(sysctl-name "sysctl.name2oid")
-			)
-			(require-any
-				(sysctl-name "hw.logicalcpu_max")
-				(sysctl-name "hw.model")
-				(sysctl-name "hw.physicalcpu_max")
-				(sysctl-name "hw.product")
-			)
-			(require-any
-				(sysctl-name "kern.hostname")
-				(sysctl-name "kern.ostype")
-				(sysctl-name "kern.version")
-			)
-			(require-any
-				(sysctl-name "kern.maxfilesperproc")
-				(sysctl-name "kern.osversion")
-			)
-			(sysctl-name "hw.cpusubfamily")
-			(sysctl-name "hw.pagesize_compat")
-			(sysctl-name "hw.physicalcpu")
-			(sysctl-name "kern.bootargs")
-			(sysctl-name "kern.bootsessionuuid")
-			(sysctl-name "kern.osrelease")
-			(sysctl-name "kern.willshutdown")
-			(sysctl-name "vm.footprint_suspend")
-		)
 	)
 )
 
 (allow system-audit)
 
 (deny system-fcntl)
+(allow system-fcntl
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow system-fcntl
 	(fcntl-command
 		F_GETFD

 		F_GETSIGSINFO)
 )
 
-(deny system-info
-	(with no-report)
-	(info-type "net.link.addr")
-)
-(deny system-info)
-
 (deny system-mac-syscall)
-(with-filter (mac-policy-name "AMFI")
-	(allow system-mac-syscall
-		(mac-syscall-number 102 90)
-	)
+(allow system-mac-syscall
+	(with report)
+	(system-attribute developer-mode)
 )
 (with-filter (mac-policy-name "Sandbox")
 	(allow system-mac-syscall
 		(mac-syscall-number 5 65)
 	)
 )
-(with-filter (mac-policy-name "Sandbox")
-	(allow system-mac-syscall
-		(mac-syscall-number 2 4 6 7 67)
-	)
-)
 
 (deny system-necp-client-action)
 

 	(%entitlement-is-bool-true "com.apple.private.kernel.override-cpumon")
 )
 
+(allow user-preference-read
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow user-preference-read
 	(require-any
 		(extension "com.apple.security.exception.shared-preference.read-only")

 	)
 )
 
+(allow managed-preference-read
+	(with report)
+	(system-attribute developer-mode)
+)
 (allow managed-preference-read
 	(require-any
 		(extension "com.apple.security.exception.managed-preference.read-only")
```
