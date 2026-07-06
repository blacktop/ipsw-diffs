## AudioConverterService

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(extension "com.apple.sandbox.container")
+		(extension-class "com.apple.aned.read-only")
+		(extension "com.apple.assets.read")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+			(require-all
+				(subpath "${HOME}/Library/Assets")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			)
+			(require-all
+				(subpath "/private/var/MobileAsset")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			)
 		)
 	)
 )

 						(extension-class "com.apple.app-sandbox.read")
 						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 						(require-any
-							(require-any
-								(subpath "/AppleInternal/Applications")
-								(subpath "/System/Developer/Applications")
-							)
 							(require-any
 								(subpath "/private/var/factory_mount/[^/]+/Applications")
 								(subpath "/private/var/personalized_automation/Applications")

 								(subpath "/private/var/personalized_factory/[^/]+/Applications")
 							)
 							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/AppleInternal/Applications")
 							(subpath "/Applications")
 							(subpath "/Developer/Applications")
+							(subpath "/System/Developer/Applications")
 							(subpath "/private/var/containers/Bundle")
 						)
 					)

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(require-any
-			(require-all
-				(%entitlement-is-present "com.apple.security.ts.tmpdir")
-				(require-any
-					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-				)
-			)
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-		)
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.identityservices.send")
+		(extension-class "com.apple.mediaserverd.read")
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 		(require-any
 			(require-all
-				(subpath "${PROCESS_TEMP_DIR}")
-				(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
-			)
-			(require-all
-				(subpath "/private/var/tmp")
-				(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
+				(%entitlement-is-present "com.apple.security.ts.tmpdir")
+				(require-any
+					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+				)
 			)
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 		)
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
 				(%entitlement-is-present "com.apple.security.ts.system-tmpdir")

 				)
 			)
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.aned.read-only")
+				(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 				(require-any
-					(require-all
-						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-						(require-any
-							(require-all
-								(extension-class "com.apple.mediaserverd.read")
-								(require-any
-									(require-all
-										(extension "com.apple.security.exception.files.absolute-path.read-only")
-										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-									)
-									(require-all
-										(extension "com.apple.security.exception.files.home-relative-path.read-only")
-										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-									)
-									(require-all
-										(extension "com.apple.security.exception.files.home-relative-path.read-write")
-										(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-									)
-								)
-							)
-							(require-any
-								(subpath "/AppleInternal/Applications")
-								(subpath "/System/Developer/Applications")
-							)
-							(require-any
-								(subpath "/private/var/factory_mount/[^/]+/Applications")
-								(subpath "/private/var/personalized_automation/Applications")
-								(subpath "/private/var/personalized_debug/Applications")
-								(subpath "/private/var/personalized_factory/[^/]+/Applications")
-							)
-							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-							(subpath "/Applications")
-							(subpath "/Developer/Applications")
-							(subpath "/private/var/containers/Bundle")
-						)
-					)
-					(require-all
-						(extension-class "com.apple.mediaserverd.read")
-						(require-any
-							(require-all
-								(extension "com.apple.security.exception.files.absolute-path.read-only")
-								(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-							)
-							(require-all
-								(extension "com.apple.security.exception.files.home-relative-path.read-only")
-								(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-							)
-							(require-all
-								(extension "com.apple.security.exception.files.home-relative-path.read-write")
-								(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-							)
-						)
+					(require-any
+						(subpath "/private/var/factory_mount/[^/]+/Applications")
+						(subpath "/private/var/personalized_automation/Applications")
+						(subpath "/private/var/personalized_debug/Applications")
+						(subpath "/private/var/personalized_factory/[^/]+/Applications")
 					)
+					(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+					(subpath "/AppleInternal/Applications")
+					(subpath "/Applications")
+					(subpath "/Developer/Applications")
+					(subpath "/System/Developer/Applications")
+					(subpath "/private/var/containers/Bundle")
 				)
 			)
 		)

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(extension "com.apple.sandbox.container")
+		(extension-class "com.apple.identityservices.send")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+			(require-all
+				(subpath "${PROCESS_TEMP_DIR}")
+				(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
+			)
+			(require-all
+				(subpath "/private/var/tmp")
+				(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
+			)
 		)
 	)
 )

 			(require-all
 				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-				(extension-class "com.apple.quicklook.readonly")
+				(extension-class "com.apple.mediaserverd.read-write")
 			)
 			(require-all
 				(extension "com.apple.librarian.ubiquity-container")
 				(require-any
 					(require-all
 						(extension-class "com.apple.mediaserverd.read-write")
-						(extension "com.apple.security.exception.files.home-relative-path.read-write")
+						(require-any
+							(extension "com.apple.security.exception.files.absolute-path.read-write")
+							(extension "com.apple.security.exception.files.home-relative-path.read-write")
+						)
 					)
 					(require-all
 						(subpath "${HOME}/Library/Mobile Documents")
-						(extension-class "com.apple.quicklook.readonly")
+						(extension-class "com.apple.mediaserverd.read-write")
 					)
 					(require-all
 						(subpath "/private/var")
 						(require-any
 							(require-all
 								(extension-class "com.apple.mediaserverd.read-write")
-								(extension "com.apple.security.exception.files.home-relative-path.read-write")
+								(require-any
+									(extension "com.apple.security.exception.files.absolute-path.read-write")
+									(extension "com.apple.security.exception.files.home-relative-path.read-write")
+								)
 							)
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 								(require-any
 									(require-all
 										(extension-class "com.apple.mediaserverd.read-write")
-										(extension "com.apple.security.exception.files.home-relative-path.read-write")
+										(require-any
+											(extension "com.apple.security.exception.files.absolute-path.read-write")
+											(extension "com.apple.security.exception.files.home-relative-path.read-write")
+										)
 									)
 									(require-all
 										(subpath "${FRONT_USER_HOME}")

 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-						(extension-class "com.apple.quicklook.readonly")
+						(extension-class "com.apple.mediaserverd.read-write")
 					)
 					(require-all
 						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-						(extension-class "com.apple.quicklook.readonly")
+						(extension-class "com.apple.mediaserverd.read-write")
 					)
 				)
 			)

 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read-write")
-				(extension "com.apple.security.exception.files.home-relative-path.read-write")
+				(require-any
+					(extension "com.apple.security.exception.files.absolute-path.read-write")
+					(extension "com.apple.security.exception.files.home-relative-path.read-write")
+				)
 			)
 			(require-all
 				(extension-class "com.apple.quicklook.readonly")

 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-				(extension-class "com.apple.quicklook.readonly")
-			)
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 				(require-any
+					(extension-class "com.apple.aned.read-only")
+					(extension-class "com.apple.app-sandbox.read")
+					(extension-class "com.apple.app-sandbox.read-write")
 					(extension-class "com.apple.mediaserverd.read")
 					(extension-class "com.apple.mediaserverd.read-write")
 					(extension-class "com.apple.quicklook.readonly")
 				)
 			)
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
 				(extension-class "com.apple.mediaserverd.read-write")
-				(require-any
-					(require-all
-						(extension "com.apple.security.exception.files.absolute-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-					)
-					(require-all
-						(extension "com.apple.security.exception.files.home-relative-path.read-write")
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-					)
-				)
 			)
 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(subpath "/private/var/MobileAsset")
+		(extension-class "com.apple.mediaserverd.read")
+		(extension "com.apple.assets.read")
+		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(require-all
-				(extension "com.apple.sandbox.container")
+				(extension "com.apple.security.exception.files.absolute-path.read-only")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			)
+			(require-all
+				(extension "com.apple.security.exception.files.absolute-path.read-write")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			)
+			(require-all
+				(extension "com.apple.security.exception.files.home-relative-path.read-only")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			)
+			(require-all
+				(extension "com.apple.security.exception.files.home-relative-path.read-write")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			)
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(require-any
+			(require-all
+				(extension "com.apple.security.exception.files.absolute-path.read-write")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			)
+			(require-all
+				(extension "com.apple.security.exception.files.home-relative-path.read-write")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			)
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "${HOME}/Library/Assets")
+		(require-any
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(extension "com.apple.assets.read")
 				(require-any
-					(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-					(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
 				)
 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(require-all
-						(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-						(require-any
-							(extension "com.apple.security.exception.files.absolute-path.read-only")
-							(extension "com.apple.security.exception.files.absolute-path.read-write")
-							(extension "com.apple.security.exception.files.home-relative-path.read-only")
-							(extension "com.apple.security.exception.files.home-relative-path.read-write")
-							(require-all
-								(extension "com.apple.assets.read")
-								(require-any
-									(require-all
-										(subpath "${HOME}/Library/Assets")
-										(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-									)
-									(require-all
-										(subpath "/private/var/MobileAsset")
-										(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(extension "com.apple.assets.read")
-						(require-any
-							(require-all
-								(subpath "${HOME}/Library/Assets")
-								(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-							)
-							(require-all
-								(subpath "/private/var/MobileAsset")
-								(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-							)
-						)
-					)
-				)
+				(extension "com.apple.assets.read")
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 			)
 		)
 	)

 )
 (allow file-read*
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
+(allow file-read*
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
 (allow file-read*
 	(require-all
 		(literal "/private/var/db/com.apple.networkextension.tracker-info")

 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
-(allow file-read*
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
 (allow file-read*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 )
 (allow file-read*
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
-		(literal "/private/var/preferences/com.apple.security.plist")
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(subpath "${HOME}/Library/Fonts")
 	)
 )
 (allow file-read*
 	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )

 )
 (allow file-read*
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(subpath "${HOME}/Library/Fonts")
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
+		(literal "/private/var/preferences/com.apple.security.plist")
 	)
 )
 (allow file-read*

 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(subpath "/private/var/MobileAsset")
+			)
+			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 				(require-any
 					(subpath "${HOME}/Library/Assets")
 					(subpath "/private/var/MobileAsset")
 				)
 			)
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-				(subpath "/private/var/MobileAsset")
-			)
 		)
 	)
 )

 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
 			(require-any
 				(subpath "/private/var/factory_mount/[^/]+/Applications")
 				(subpath "/private/var/personalized_automation/Applications")

 				(subpath "/private/var/personalized_factory/[^/]+/Applications")
 			)
 			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
 			(subpath "/Applications")
 			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
 			(subpath "/private/var/containers/Bundle")
 		)
 	)

 )
 (allow file-read-data
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
+(allow file-read-data
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
 (allow file-read-data
 	(require-all
 		(literal "/private/var/db/com.apple.networkextension.tracker-info")

 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
-(allow file-read-data
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
 (allow file-read-data
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 )
 (allow file-read-data
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
-		(literal "/private/var/preferences/com.apple.security.plist")
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(subpath "${HOME}/Library/Fonts")
 	)
 )
 (allow file-read-data
 	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )

 )
 (allow file-read-data
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(subpath "${HOME}/Library/Fonts")
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
+		(literal "/private/var/preferences/com.apple.security.plist")
 	)
 )
 (allow file-read-data

 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(subpath "/private/var/MobileAsset")
+			)
+			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 				(require-any
 					(subpath "${HOME}/Library/Assets")
 					(subpath "/private/var/MobileAsset")
 				)
 			)
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-				(subpath "/private/var/MobileAsset")
-			)
 		)
 	)
 )
 (allow file-read-data
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
-		(extension "com.apple.revisiond.staging")
+		(vnode-type DIRECTORY SYMLINK)
+		(extension "com.apple.revisiond.revision")
 		(require-any
 			(require-all
-				(extension "com.apple.revisiond.revision")
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(require-any
-					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-				)
-			)
-			(require-all
+				(extension "com.apple.revisiond.staging")
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
 					(subpath "/private/var/.DocumentRevisions-V100/staging")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 				)
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+				)
+			)
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+				)
 				(require-any
 					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
 					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 					(require-all
-						(extension "com.apple.revisiond.revision")
+						(extension "com.apple.revisiond.staging")
 						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 						)
 						(require-any
 							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")

 )
 (allow file-read-data
 	(require-all
-		(vnode-type SYMLINK)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(extension "com.apple.revisiond.revision")
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(require-any
-					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-				)
-			)
-			(require-all
-				(extension "com.apple.revisiond.staging")
 				(require-any
 					(require-all
-						(extension "com.apple.revisiond.revision")
-						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-						)
-						(require-any
-							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-						)
-					)
-					(require-all
+						(extension "com.apple.revisiond.staging")
 						(require-any
 							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
 							(subpath "/private/var/.DocumentRevisions-V100/staging")
 							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 						)
+						(require-any
+							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+						)
+					)
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+						)
 						(require-any
 							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
 							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 							(require-all
-								(extension "com.apple.revisiond.revision")
+								(extension "com.apple.revisiond.staging")
 								(require-any
-									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 								)
 								(require-any
 									(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")

 					)
 				)
 			)
+			(require-all
+				(extension "com.apple.revisiond.staging")
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+				)
+			)
 		)
 	)
 )

 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
 			(require-any
 				(subpath "/private/var/factory_mount/[^/]+/Applications")
 				(subpath "/private/var/personalized_automation/Applications")

 				(subpath "/private/var/personalized_factory/[^/]+/Applications")
 			)
 			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
 			(subpath "/Applications")
 			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
 			(subpath "/private/var/containers/Bundle")
 		)
 	)

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )

 			(require-all
 				(vnode-type DIRECTORY)
 				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)
 				(require-any
-					(extension "com.apple.revisiond.staging")
+					(extension "com.apple.revisiond.revision")
 					(require-all
 						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 						)
-						(extension "com.apple.revisiond.revision")
+						(extension "com.apple.revisiond.staging")
 					)
 				)
 			)
 			(require-all
 				(vnode-type REGULAR-FILE)
 				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
 					(require-all
 						(require-any
 							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 						)
-						(extension "com.apple.revisiond.revision")
-					)
-				)
-			)
-			(require-all
-				(vnode-type SYMLINK)
-				(require-any
-					(require-all
 						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+							(extension "com.apple.revisiond.revision")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+								)
+								(extension "com.apple.revisiond.staging")
+							)
 						)
-						(extension "com.apple.revisiond.revision")
 					)
 					(require-all
 						(require-any

 							(subpath "/private/var/.DocumentRevisions-V100/staging")
 							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 						)
+						(extension "com.apple.revisiond.staging")
+					)
+				)
+			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+				)
+				(require-any
+					(extension "com.apple.revisiond.revision")
+					(require-all
 						(require-any
-							(extension "com.apple.revisiond.staging")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-								)
-								(extension "com.apple.revisiond.revision")
-							)
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 						)
+						(extension "com.apple.revisiond.staging")
 					)
 				)
 			)

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/preferences/com.apple.security.plist")
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )

 		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
+		(literal "/private/var/preferences/com.apple.security.plist")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")

 		)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(subpath "${HOME}/Library/Fonts")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var/containers/Data/System/com.apple.geod")

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(literal "/private/var/db/com.apple.networkextension.tracker-info")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )

 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
 			(require-any
 				(subpath "/private/var/factory_mount/[^/]+/Applications")
 				(subpath "/private/var/personalized_automation/Applications")

 				(subpath "/private/var/personalized_factory/[^/]+/Applications")
 			)
 			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
 			(subpath "/Applications")
 			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
 			(subpath "/private/var/containers/Bundle")
 		)
 	)

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/db/com.apple.networkextension.tracker-info")
+		(literal "/private/var/preferences/com.apple.security.plist")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
 (allow file-read-metadata
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
-		(literal "/private/var/preferences/com.apple.security.plist")
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(subpath "${HOME}/Library/Fonts")
 	)
 )
 (allow file-read-metadata

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type DIRECTORY SYMLINK)
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any
 			(require-all

 					(require-all
 						(require-any
 							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 						)

 			(require-all
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type SYMLINK)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")

 							(require-all
 								(require-any
 									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+									(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 									(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 								)

 					(require-all
 						(require-any
 							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 						)

 			(require-all
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)

 			(require-all
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
 				)

 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(subpath "/private/var/MobileAsset")
+			)
+			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 				(require-any
 					(subpath "${HOME}/Library/Assets")
 					(subpath "/private/var/MobileAsset")
 				)
 			)
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-				(subpath "/private/var/MobileAsset")
-			)
 		)
 	)
 )

 )
 (allow file-read-xattr
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(literal "/private/var/db/com.apple.networkextension.tracker-info")

 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
 (allow file-read-xattr
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 )
 (allow file-read-xattr
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
-		(literal "/private/var/preferences/com.apple.security.plist")
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(subpath "${HOME}/Library/Fonts")
 	)
 )
 (allow file-read-xattr
 	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(literal "/private/var/preferences/com.apple.networkd.plist")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )

 )
 (allow file-read-xattr
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(subpath "${HOME}/Library/Fonts")
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
+		(literal "/private/var/preferences/com.apple.security.plist")
 	)
 )
 (allow file-read-xattr

 		(require-any
 			(require-all
 				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(subpath "/private/var/MobileAsset")
+			)
+			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 				(require-any
 					(subpath "${HOME}/Library/Assets")
 					(subpath "/private/var/MobileAsset")
 				)
 			)
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-				(subpath "/private/var/MobileAsset")
-			)
 		)
 	)
 )
 (allow file-read-xattr
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
-		(extension "com.apple.revisiond.staging")
+		(vnode-type DIRECTORY SYMLINK)
+		(extension "com.apple.revisiond.revision")
 		(require-any
 			(require-all
-				(extension "com.apple.revisiond.revision")
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(require-any
-					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-				)
-			)
-			(require-all
+				(extension "com.apple.revisiond.staging")
 				(require-any
 					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
 					(subpath "/private/var/.DocumentRevisions-V100/staging")
 					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 				)
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+				)
+			)
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+				)
 				(require-any
 					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
 					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 					(require-all
-						(extension "com.apple.revisiond.revision")
+						(extension "com.apple.revisiond.staging")
 						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 						)
 						(require-any
 							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")

 )
 (allow file-read-xattr
 	(require-all
-		(vnode-type SYMLINK)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(require-all
 				(extension "com.apple.revisiond.revision")
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(require-any
-					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-				)
-			)
-			(require-all
-				(extension "com.apple.revisiond.staging")
 				(require-any
 					(require-all
-						(extension "com.apple.revisiond.revision")
-						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-						)
-						(require-any
-							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-						)
-					)
-					(require-all
+						(extension "com.apple.revisiond.staging")
 						(require-any
 							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
 							(subpath "/private/var/.DocumentRevisions-V100/staging")
 							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 						)
+						(require-any
+							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+						)
+					)
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+						)
 						(require-any
 							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
 							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 							(require-all
-								(extension "com.apple.revisiond.revision")
+								(extension "com.apple.revisiond.staging")
 								(require-any
-									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+									(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/.DocumentRevisions-V100/staging")
+									(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
 								)
 								(require-any
 									(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")

 					)
 				)
 			)
+			(require-all
+				(extension "com.apple.revisiond.staging")
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+				)
+			)
 		)
 	)
 )

 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
 		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
 			(require-any
 				(subpath "/private/var/factory_mount/[^/]+/Applications")
 				(subpath "/private/var/personalized_automation/Applications")

 				(subpath "/private/var/personalized_factory/[^/]+/Applications")
 			)
 			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
 			(subpath "/Applications")
 			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
 			(subpath "/private/var/containers/Bundle")
 		)
 	)

 			)
 			(require-all
 				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-			(require-all
-				(vnode-type SYMLINK)
 				(require-any
 					(require-all
 						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 					)
 				)
 			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(extension "com.apple.revisiond.staging")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
 		)
 	)
 )

 )
 (allow file-write*
 	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
 		(require-any
 			(require-all

 			)
 			(require-all
 				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-			(require-all
-				(vnode-type SYMLINK)
 				(require-any
 					(require-all
 						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 					)
 				)
 			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(extension "com.apple.revisiond.staging")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
 		)
 	)
 )

 )
 (allow file-write-create
 	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
 		(require-any
 			(require-all

 			)
 			(require-all
 				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(extension "com.apple.revisiond.staging")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-			(require-all
-				(vnode-type SYMLINK)
 				(require-any
 					(require-all
 						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 					)
 				)
 			)
+			(require-all
+				(vnode-type SYMLINK)
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/.DocumentRevisions-V100/staging")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+				)
+				(require-any
+					(extension "com.apple.revisiond.staging")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
 		)
 	)
 )

 )
 (allow file-write-unlink
 	(require-all
-		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
 		(extension "com.apple.tcc.kTCCServiceAddressBook")
 		(require-any
 			(require-all

 			(require-all
 				(system-attribute virtual-device)
 				(require-any
-					(iokit-registry-entry-class "AppleJPEGDriverUserClient")
+					(iokit-registry-entry-class "AppleKeyStoreUserClient")
 					(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationUserClient")
 					(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")
 				)

 			(iokit-registry-entry-class "AGXCommandQueue")
 			(iokit-registry-entry-class "AGXDevice")
 			(iokit-registry-entry-class "AGXSharedUserClient")
+			(iokit-registry-entry-class "IOAccelContext2")
 			(iokit-registry-entry-class "IOGPUDeviceUserClient")
 			(require-any
 				(iokit-connection "IOGPU")

 			)
 			(require-any
 				(iokit-registry-entry-class "IOAccelContext")
-				(iokit-registry-entry-class "IOAccelContext2")
 				(iokit-registry-entry-class "IOAccelDevice")
 				(iokit-registry-entry-class "IOAccelDevice2")
 				(iokit-registry-entry-class "IOAccelSharedUserClient")

 (allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "AGXAcceleratorG*")
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-	)
-)
-(allow iokit-open-service
-	(require-all
-		(require-any
-			(iokit-registry-entry-class "AppleCLCD*")
-			(iokit-registry-entry-class "AppleParavirtDisplay*")
-		)
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
 (allow iokit-open-service

 )
 (allow iokit-open-service
 	(require-all
-		(iokit-registry-entry-class "AppleParavirtGPU*")
+		(require-any
+			(iokit-registry-entry-class "AppleCLCD*")
+			(iokit-registry-entry-class "AppleParavirtDisplay*")
+			(iokit-registry-entry-class "AppleParavirtGPU*")
+		)
 		(require-any
 			(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 			(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")

 	)
 )
 
-(allow mach-lookup
-	(require-all
-		(xpc-service-name "com.apple.ImageIOXPCService")
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.ABDatabaseDoctor")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(xpc-service-name "com.apple.AGXCompilerService*")
 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(xpc-service-name ".viewservice")
-		(%entitlement-is-bool-true "com.apple.security.ts.viewservice.client")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(xpc-service-name "com.apple.MTLCompilerService")
 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(xpc-service-name "com.apple.ImageIOXPCService")
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(xpc-service-name ".viewservice")
+		(%entitlement-is-bool-true "com.apple.security.ts.viewservice.client")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.accountsd.accountmanager")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.contactsd")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities")
+		(global-name "com.apple.cmfsyncagent.embedded.auth")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.accountsd.accountmanager")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.identityservicesd.idquery.embedded.auth")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.spotlight.IndexAgent")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(%entitlement-is-present "com.apple.security.ts.webkit-client")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.cmfsyncagent.embedded.auth")
+		(global-name "com.apple.ABDatabaseDoctor")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.identityservicesd.idquery.embedded.auth")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.spotlight.IndexDelegateAgent")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.spotlight.IndexDelegateAgent")
+		(global-name "com.apple.spotlight.IndexAgent")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )

 			)
 			(require-all
 				(socket-option-name SO_RCVBUF)
+				(%entitlement-is-bool-true "com.apple.security.network.server")
+			)
+			(require-all
+				(socket-option-name SO_REUSEADDR)
 				(require-any
 					(%entitlement-is-bool-true "com.apple.security.network.client")
 					(%entitlement-is-bool-true "com.apple.security.network.server")
 				)
 			)
-			(require-all
-				(socket-option-name SO_REUSEADDR)
-				(%entitlement-is-bool-true "com.apple.security.network.server")
-			)
 		)
 	)
 )

 )
 (allow sysctl-read
 	(require-all
-		(sysctl-name "net.routetable.*")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow sysctl-read
-	(require-all
-		(sysctl-name "net.statistics")
+		(require-any
+			(sysctl-name "kern.nisdomainname")
+			(sysctl-name "net.statistics")
+		)
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )

 )
 (allow sysctl-read
 	(require-all
-		(sysctl-name "kern.nisdomainname")
+		(sysctl-name "net.routetable.*")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.security.network.client")
 			(%entitlement-is-bool-true "com.apple.security.network.server")

 
 (allow system-fsctl
 	(require-all
-		(fsctl-command APFSIOC_GET_DIR_STATS_EXT)
+		(fsctl-command APFSIOC_GET_DIR_STATS)
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )

 )
 (allow system-fsctl
 	(require-all
-		(fsctl-command APFSIOC_GET_DIR_STATS)
+		(fsctl-command APFSIOC_GET_DIR_STATS_EXT)
 		(require-any
 			(%entitlement-is-bool-true "com.apple.security.network.client")
 			(%entitlement-is-bool-true "com.apple.security.network.server")

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.corevideo")
+		(preference-domain "com.apple.avfoundation")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.coreaudio")
+		(preference-domain "com.apple.coremedia")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.avfoundation")
+		(preference-domain "com.apple.coreaudio")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.logging")
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
+		(preference-domain "com.apple.conference")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )
 (allow user-preference-read

 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.coremedia")
+		(preference-domain "com.apple.corevideo")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )

 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 		(require-any
-			(preference-domain "com.apple.conference")
-			(preference-domain "com.apple.ids")
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
 		)
 	)
 )
 (allow user-preference-read
 	(require-all
-		(preference-domain "com.apple.marco")
+		(preference-domain "com.apple.ids")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")

 )
 (allow user-preference-read
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
 		(require-any
-			(preference-domain "com.apple.conference")
-			(preference-domain "com.apple.ids")
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
 		)
 	)
 )
 (allow user-preference-read
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
 		(require-any
-			(preference-domain "com.apple.conference")
-			(preference-domain "com.apple.ids")
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(preference-domain "com.apple.mobileipod")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+			(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		)
+	)
+)
+(allow user-preference-read
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(require-any
+			(preference-domain "com.apple.avfoundation")
+			(preference-domain "com.apple.coreaudio")
+			(preference-domain "com.apple.coremedia")
+			(preference-domain "com.apple.corevideo")
 		)
 	)
 )

 		)
 	)
 )
-(allow user-preference-read
-	(require-all
-		(preference-domain "com.apple.mobileipod")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-			(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		)
-	)
-)
-(allow user-preference-read
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-any
-			(preference-domain "com.apple.avfoundation")
-			(preference-domain "com.apple.coreaudio")
-			(preference-domain "com.apple.coremedia")
-			(preference-domain "com.apple.corevideo")
-		)
-	)
-)
 (allow user-preference-read
 	(require-any
 		(preference-domain "com.apple.NanoRegistry")

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.corevideo")
+		(preference-domain "com.apple.avfoundation")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.coreaudio")
+		(preference-domain "com.apple.coremedia")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.avfoundation")
+		(preference-domain "com.apple.coreaudio")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.logging")
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
+		(preference-domain "com.apple.conference")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )
 (allow managed-preference-read

 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.coremedia")
+		(preference-domain "com.apple.corevideo")
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 	)
 )

 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 		(require-any
-			(preference-domain "com.apple.conference")
-			(preference-domain "com.apple.ids")
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
 		)
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(preference-domain "com.apple.marco")
+		(preference-domain "com.apple.ids")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")

 )
 (allow managed-preference-read
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
 		(require-any
-			(preference-domain "com.apple.conference")
-			(preference-domain "com.apple.ids")
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
 		)
 	)
 )
 (allow managed-preference-read
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
 		(require-any
-			(preference-domain "com.apple.conference")
-			(preference-domain "com.apple.ids")
+			(preference-domain "com.apple.logging")
+			(preference-domain "com.apple.marco")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(preference-domain "com.apple.mobileipod")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+			(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		)
+	)
+)
+(allow managed-preference-read
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(require-any
+			(preference-domain "com.apple.avfoundation")
+			(preference-domain "com.apple.coreaudio")
+			(preference-domain "com.apple.coremedia")
+			(preference-domain "com.apple.corevideo")
 		)
 	)
 )

 		)
 	)
 )
-(allow managed-preference-read
-	(require-all
-		(preference-domain "com.apple.mobileipod")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-			(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-			(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		)
-	)
-)
-(allow managed-preference-read
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-any
-			(preference-domain "com.apple.avfoundation")
-			(preference-domain "com.apple.coreaudio")
-			(preference-domain "com.apple.coremedia")
-			(preference-domain "com.apple.corevideo")
-		)
-	)
-)
 (allow managed-preference-read
 	(require-any
 		(preference-domain "com.apple.NanoRegistry")
```
