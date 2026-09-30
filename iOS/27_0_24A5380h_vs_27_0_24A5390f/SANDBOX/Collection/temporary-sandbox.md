## temporary-sandbox

> Group: ⬆️ Updated

```diff

 	(signing-identifier "com.apple.anomalydetectiond")
 ))
 (define (_g13 _)
+	(require-all
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+	(signing-identifier "com.apple.fileindexerd")
+))
+(define (_g14 _)
 	(require-all
 	(require-any
 		(subpath "${FRONT_USER_HOME}")

 	)
 	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
 ))
-(define (_g14 _)
+(define (_g15 _)
 	(require-any
-	(_g13 "")
+	(_g14 "")
 	(require-all
 		(subpath "/private/var/PersonaVolumes")
 		(require-any
-			(_g13 "")
+			(_g14 "")
 			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/|$)")
 		)
 	)
 ))
-(define (_g15 _)
+(define (_g16 _)
 	(require-all
 	(extension-class "com.apple.StreamingUnzipService")
 	(signing-identifier "com.apple.appplaceholdersyncd")
 	(subpath "/private/var")
 	(extension "com.apple.sandbox.container")
-	(_g14 "")
-))
-(define (_g16 _)
-	(require-any
 	(_g15 "")
+))
+(define (_g17 _)
+	(require-any
+	(_g16 "")
 	(require-all
 		(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
 		(extension-class "com.apple.StreamingUnzipService")
 		(signing-identifier "com.apple.appplaceholdersyncd")
 		(subpath "/private/var")
 		(extension "com.apple.sandbox.container")
-		(_g14 "")
+		(_g15 "")
 	)
 	(require-all
 		(subpath "/private/var/containers/Shared/SystemGroup")
 		(require-any
-			(_g15 "")
+			(_g16 "")
 			(regex #"^/private/var/containers/Shared/SystemGroup/[^/]+(/|$)")
 		)
 	)
 ))
-(define (_g17 _)
+(define (_g18 _)
 	(require-all
 	(extension "com.apple.sandbox.system-group")
 	(require-any
 		(require-all
 			(%entitlement-is-present "com.apple.security.system-group-containers")
 			(signing-identifier "com.apple.bookassetd")
-			(_g16 "")
+			(_g17 "")
 		)
 		(require-all
 			(%entitlement-is-present "com.apple.security.system-groups")
 			(require-any
-				(_g15 "")
+				(_g16 "")
 				(require-all
 					(signing-identifier "com.apple.bookassetd")
-					(_g16 "")
+					(_g17 "")
 				)
 			)
 		)

 			(signing-identifier "com.apple.appplaceholdersyncd")
 			(subpath "/private/var")
 			(extension "com.apple.sandbox.container")
-			(_g14 "")
+			(_g15 "")
 		)
 	)
 ))
-(define (_g18 _)
+(define (_g19 _)
 	(require-all
 	(subpath "${HOME}/Library/BulletinDistributor/Attachments")
 	(require-any

 		(signing-identifier "com.apple.Carousel")
 	)
 ))
-(define (_g19 _)
-	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
 (define (_g20 _)
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+(define (_g21 _)
 	(require-any
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")

 	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
-(define (_g21 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read")
-	(signing-identifier "com.apple.linkd")
-	(_g20 "")
-))
 (define (_g22 _)
-	(require-any
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(signing-identifier "com.apple.mediaplaybackd")
-		(require-any
-			(extension "com.apple.mediaserverd.read-write")
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(require-all
-						(signing-identifier "com.apple.linkd")
-						(_g20 "")
-					)
-					(require-all
-						(signing-identifier "com.apple.mediaplaybackd")
-						(require-any
-							(_g19 "")
-							(extension "com.apple.mediaserverd.read")
-						)
-					)
-				)
-			)
-		)
-	)
-	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+	(extension-class "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.linkd")
+	(_g21 "")
 ))
 (define (_g23 _)
-	(require-all
-	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.momentsd")
-			(_g22 "")
-		)
-		(require-all
-			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-			(require-any
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
 				(extension-class "com.apple.mediaserverd.read")
-				(extension-class "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.app-sandbox.read-write")
-					(signing-identifier "com.apple.momentsd")
-					(_g22 "")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(_g21 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(_g20 "")
+							(extension "com.apple.mediaserverd.read")
+						)
+					)
 				)
 			)
 		)
-		(subpath "${HOME}/Library/com.apple.momentsd")
 	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g24 _)
-	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+	(require-all
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.momentsd")
+			(_g23 "")
+		)
+		(require-all
+			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+			(require-any
+				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.app-sandbox.read-write")
+					(signing-identifier "com.apple.momentsd")
+					(_g23 "")
+				)
+			)
+		)
+		(subpath "${HOME}/Library/com.apple.momentsd")
+	)
+))
 (define (_g25 _)
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+(define (_g26 _)
 	(require-any
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")

 	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
-(define (_g26 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read")
-	(signing-identifier "com.apple.linkd")
-	(_g25 "")
-))
 (define (_g27 _)
-	(require-any
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(signing-identifier "com.apple.mediaplaybackd")
-		(require-any
-			(extension "com.apple.mediaserverd.read-write")
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(require-all
-						(signing-identifier "com.apple.linkd")
-						(_g25 "")
-					)
-					(require-all
-						(signing-identifier "com.apple.mediaplaybackd")
-						(require-any
-							(_g24 "")
-							(extension "com.apple.mediaserverd.read")
-						)
-					)
-				)
-			)
-		)
-	)
-	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+	(extension-class "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.linkd")
+	(_g26 "")
 ))
 (define (_g28 _)
-	(require-all
-	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.momentsd")
-			(_g27 "")
-		)
-		(require-all
-			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-			(require-any
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
 				(extension-class "com.apple.mediaserverd.read")
-				(extension-class "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.app-sandbox.read-write")
-					(signing-identifier "com.apple.momentsd")
-					(_g27 "")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(_g26 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(_g25 "")
+							(extension "com.apple.mediaserverd.read")
+						)
+					)
 				)
 			)
 		)
-		(subpath "${HOME}/Library/com.apple.momentsd")
 	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g29 _)
-	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+	(require-all
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.momentsd")
+			(_g28 "")
+		)
+		(require-all
+			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+			(require-any
+				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.app-sandbox.read-write")
+					(signing-identifier "com.apple.momentsd")
+					(_g28 "")
+				)
+			)
+		)
+		(subpath "${HOME}/Library/com.apple.momentsd")
+	)
+))
 (define (_g30 _)
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+(define (_g31 _)
 	(require-any
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")

 	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
-(define (_g31 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read")
-	(signing-identifier "com.apple.linkd")
-	(_g30 "")
-))
 (define (_g32 _)
-	(require-any
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(signing-identifier "com.apple.mediaplaybackd")
-		(require-any
-			(extension "com.apple.mediaserverd.read-write")
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(require-all
-						(signing-identifier "com.apple.linkd")
-						(_g30 "")
-					)
-					(require-all
-						(signing-identifier "com.apple.mediaplaybackd")
-						(require-any
-							(_g29 "")
-							(extension "com.apple.mediaserverd.read")
-						)
-					)
-				)
-			)
-		)
-	)
-	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+	(extension-class "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.linkd")
+	(_g31 "")
 ))
 (define (_g33 _)
-	(require-all
-	(signing-identifier "com.apple.momentsd")
 	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.momentsd")
-			(_g32 "")
-		)
-		(require-all
-			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-			(require-any
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
 				(extension-class "com.apple.mediaserverd.read")
-				(extension-class "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.app-sandbox.read-write")
-					(signing-identifier "com.apple.momentsd")
-					(_g32 "")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(_g31 "")
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(_g30 "")
+							(extension "com.apple.mediaserverd.read")
+						)
+					)
 				)
 			)
 		)
-		(subpath "${HOME}/Library/com.apple.momentsd")
 	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g34 _)
-	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+	(require-all
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.momentsd")
+			(_g33 "")
+		)
+		(require-all
+			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+			(require-any
+				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.app-sandbox.read-write")
+					(signing-identifier "com.apple.momentsd")
+					(_g33 "")
+				)
+			)
+		)
+		(subpath "${HOME}/Library/com.apple.momentsd")
+	)
+))
 (define (_g35 _)
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+(define (_g36 _)
 	(require-any
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")

 	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
-(define (_g36 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read")
-	(signing-identifier "com.apple.linkd")
-	(_g35 "")
-))
 (define (_g37 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.linkd")
+	(_g36 "")
+))
+(define (_g38 _)
 	(require-any
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")

 				(require-any
 					(require-all
 						(signing-identifier "com.apple.linkd")
-						(_g35 "")
+						(_g36 "")
 					)
 					(require-all
 						(signing-identifier "com.apple.mediaplaybackd")
 						(require-any
-							(_g34 "")
+							(_g35 "")
 							(extension "com.apple.mediaserverd.read")
 						)
 					)

 	)
 	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
-(define (_g38 _)
+(define (_g39 _)
 	(require-all
 	(signing-identifier "com.apple.momentsd")
 	(require-any
 		(require-all
 			(extension-class "com.apple.mediaserverd.read-write")
 			(signing-identifier "com.apple.momentsd")
-			(_g37 "")
+			(_g38 "")
 		)
 		(require-all
 			(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 				(require-all
 					(extension-class "com.apple.app-sandbox.read-write")
 					(signing-identifier "com.apple.momentsd")
-					(_g37 "")
+					(_g38 "")
 				)
 			)
 		)
 		(subpath "${HOME}/Library/com.apple.momentsd")
 	)
 ))
-(define (_g39 _)
-	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
 (define (_g40 _)
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+(define (_g41 _)
 	(require-any
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")

 	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
-(define (_g41 _)
+(define (_g42 _)
 	(require-all
 	(extension-class "com.apple.app-sandbox.read")
 	(signing-identifier "com.apple.linkd")
-	(_g40 "")
+	(_g41 "")
 ))
-(define (_g42 _)
+(define (_g43 _)
 	(require-any
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")

 				(require-any
 					(require-all
 						(signing-identifier "com.apple.linkd")
-						(_g40 "")
+						(_g41 "")
 					)
 					(require-all
 						(signing-identifier "com.apple.mediaplaybackd")
 						(require-any
-							(_g39 "")
+							(_g40 "")
 							(extension "com.apple.mediaserverd.read")
 						)
 					)

 	)
 	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
-(define (_g43 _)
-	(require-all
-	(signing-identifier "com.apple.momentsd")
-	(require-any
-		(require-all
-			(extension-class "com.apple.mediaserverd.read-write")
-			(signing-identifier "com.apple.momentsd")
-			(_g42 "")
-		)
-		(require-all
-			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-			(require-any
-				(extension-class "com.apple.mediaserverd.read")
-				(extension-class "com.apple.mediaserverd.read-write")
-				(require-all
-					(extension-class "com.apple.app-sandbox.read-write")
-					(signing-identifier "com.apple.momentsd")
-					(_g42 "")
-				)
-			)
-		)
-		(subpath "${HOME}/Library/com.apple.momentsd")
-	)
-))
 (define (_g44 _)
+	(require-all
+	(signing-identifier "com.apple.momentsd")
+	(require-any
+		(require-all
+			(extension-class "com.apple.mediaserverd.read-write")
+			(signing-identifier "com.apple.momentsd")
+			(_g43 "")
+		)
+		(require-all
+			(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+			(require-any
+				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.mediaserverd.read-write")
+				(require-all
+					(extension-class "com.apple.app-sandbox.read-write")
+					(signing-identifier "com.apple.momentsd")
+					(_g43 "")
+				)
+			)
+		)
+		(subpath "${HOME}/Library/com.apple.momentsd")
+	)
+))
+(define (_g45 _)
 	(require-all
 	(extension-class "com.apple.app-sandbox.read-write")
 	(require-any
-		(_g43 "")
+		(_g44 "")
 		(require-all
 			(subpath "/private/var")
 			(require-any
-				(_g43 "")
+				(_g44 "")
 				(require-all
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 					(require-any

 						(require-all
 							(signing-identifier "com.apple.mediaplaybackd")
 							(require-any
-								(_g39 "")
-								(_g41 "")
+								(_g40 "")
+								(_g42 "")
 								(require-all
 									(require-any
 										(subpath "${FRONT_USER_HOME}")
 										(subpath "${HOME}")
 									)
 									(require-any
-										(_g41 "")
+										(_g42 "")
 										(require-all
 											(subpath "/private/var")
 											(require-any
-												(_g41 "")
+												(_g42 "")
 												(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 											)
 										)

 		)
 	)
 ))
-(define (_g45 _)
+(define (_g46 _)
 	(require-all
 	(require-any
 		(subpath "${FRONT_USER_HOME}")

 	)
 	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
 ))
-(define (_g46 _)
+(define (_g47 _)
 	(require-any
-	(_g45 "")
+	(_g46 "")
 	(require-all
 		(subpath "/private/var/PersonaVolumes")
 		(require-any
-			(_g45 "")
+			(_g46 "")
 			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/|$)")
 		)
 	)
 ))
-(define (_g47 _)
+(define (_g48 _)
 	(require-all
 	(extension-class "com.apple.StreamingUnzipService")
 	(signing-identifier "com.apple.appplaceholdersyncd")
 	(subpath "/private/var")
 	(extension "com.apple.sandbox.container")
-	(_g46 "")
-))
-(define (_g48 _)
-	(require-any
 	(_g47 "")
+))
+(define (_g49 _)
+	(require-any
+	(_g48 "")
 	(require-all
 		(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
 		(extension-class "com.apple.StreamingUnzipService")
 		(signing-identifier "com.apple.appplaceholdersyncd")
 		(subpath "/private/var")
 		(extension "com.apple.sandbox.container")
-		(_g46 "")
+		(_g47 "")
 	)
 	(require-all
 		(subpath "/private/var/containers/Shared/SystemGroup")
 		(require-any
-			(_g47 "")
+			(_g48 "")
 			(regex #"^/private/var/containers/Shared/SystemGroup/[^/]+(/|$)")
 		)
 	)
 ))
-(define (_g49 _)
+(define (_g50 _)
 	(require-all
 	(extension "com.apple.sandbox.system-group")
 	(require-any
 		(require-all
 			(%entitlement-is-present "com.apple.security.system-group-containers")
 			(signing-identifier "com.apple.bookassetd")
-			(_g48 "")
+			(_g49 "")
 		)
 		(require-all
 			(%entitlement-is-present "com.apple.security.system-groups")
 			(require-any
-				(_g47 "")
+				(_g48 "")
 				(require-all
 					(signing-identifier "com.apple.bookassetd")
-					(_g48 "")
+					(_g49 "")
 				)
 			)
 		)

 			(signing-identifier "com.apple.appplaceholdersyncd")
 			(subpath "/private/var")
 			(extension "com.apple.sandbox.container")
-			(_g46 "")
+			(_g47 "")
 		)
 	)
 ))
-(define (_g50 _)
-	(require-any
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(signing-identifier "com.apple.mediaplaybackd")
-		(require-any
-			(extension "com.apple.mediaserverd.read-write")
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(require-all
-						(signing-identifier "com.apple.linkd")
-						(require-any
-							(require-any
-								(subpath "/private/var/factory_mount/[^/]+/Applications")
-								(subpath "/private/var/personalized_automation/Applications")
-								(subpath "/private/var/personalized_debug/Applications")
-								(subpath "/private/var/personalized_factory/[^/]+/Applications")
-							)
-							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-							(subpath "/AppleInternal/Applications")
-							(subpath "/Applications")
-							(subpath "/Developer/Applications")
-							(subpath "/System/Developer/Applications")
-							(subpath "/private/var/containers/Bundle")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.mediaplaybackd")
-						(require-any
-							(extension "com.apple.mediaserverd.read")
-							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
-						)
-					)
-				)
-			)
-		)
-	)
-	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-))
 (define (_g51 _)
 	(require-any
 	(require-all

 	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g54 _)
-	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+	(require-any
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read-write")
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.linkd")
+						(require-any
+							(require-any
+								(subpath "/private/var/factory_mount/[^/]+/Applications")
+								(subpath "/private/var/personalized_automation/Applications")
+								(subpath "/private/var/personalized_debug/Applications")
+								(subpath "/private/var/personalized_factory/[^/]+/Applications")
+							)
+							(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+							(subpath "/AppleInternal/Applications")
+							(subpath "/Applications")
+							(subpath "/Developer/Applications")
+							(subpath "/System/Developer/Applications")
+							(subpath "/private/var/containers/Bundle")
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(extension "com.apple.mediaserverd.read")
+							(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
+						)
+					)
+				)
+			)
+		)
+	)
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+))
 (define (_g55 _)
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd"))
+(define (_g56 _)
 	(require-any
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")

 	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
-(define (_g56 _)
+(define (_g57 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read")
 	(require-any
 		(require-all
 			(signing-identifier "com.apple.linkd")
-			(_g55 "")
+			(_g56 "")
 		)
 		(require-all
 			(signing-identifier "com.apple.mediaplaybackd")
 			(require-any
-				(_g54 "")
+				(_g55 "")
 				(extension "com.apple.mediaserverd.read")
 			)
 		)
 	)
 ))
-(define (_g57 _)
+(define (_g58 _)
 	(require-any
-	(_g56 "")
+	(_g57 "")
 	(extension "com.apple.mediaserverd.read-write")
 ))
-(define (_g58 _)
+(define (_g59 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read-write")
 	(signing-identifier "com.apple.mediaplaybackd")
-	(_g57 "")
-))
-(define (_g59 _)
-	(require-any
 	(_g58 "")
-	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g60 _)
-	(require-all
-	(extension-class "com.apple.app-sandbox.read-write")
-	(signing-identifier "com.apple.momentsd")
+	(require-any
 	(_g59 "")
+	(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 ))
 (define (_g61 _)
 	(require-all
-	(extension-class "com.apple.mediaserverd.read-write")
+	(extension-class "com.apple.app-sandbox.read-write")
 	(signing-identifier "com.apple.momentsd")
-	(_g59 "")
+	(_g60 "")
 ))
 (define (_g62 _)
 	(require-all
-	(extension-class "com.apple.app-sandbox.read")
-	(signing-identifier "com.apple.linkd")
-	(_g55 "")
+	(extension-class "com.apple.mediaserverd.read-write")
+	(signing-identifier "com.apple.momentsd")
+	(_g60 "")
 ))
 (define (_g63 _)
+	(require-all
+	(extension-class "com.apple.app-sandbox.read")
+	(signing-identifier "com.apple.linkd")
+	(_g56 "")
+))
+(define (_g64 _)
 	(require-any
-	(_g54 "")
-	(_g62 "")
+	(_g55 "")
+	(_g63 "")
 	(require-all
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
 		(require-any
-			(_g62 "")
+			(_g63 "")
 			(require-all
 				(subpath "/private/var")
 				(require-any
-					(_g62 "")
+					(_g63 "")
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 				)
 			)
 		)
 	)
 ))
-(define (_g64 _)
+(define (_g65 _)
 	(require-all
 	(extension-class "com.apple.aned.read-only")
 	(signing-identifier "com.apple.linkd")
-	(_g55 "")
+	(_g56 "")
 ))
-(define (_g65 _)
+(define (_g66 _)
 	(require-all
 	(signing-identifier "com.apple.filederivatived")
 	(extension "com.apple.app-sandbox.read")
 ))
-(define (_g66 _)
+(define (_g67 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read")
 	(require-any

 		)
 	)
 ))
-(define (_g67 _)
+(define (_g68 _)
 	(require-all
 	(require-any
 		(subpath "${FRONT_USER_HOME}")

 	)
 	(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/|$)")
 ))
-(define (_g68 _)
+(define (_g69 _)
 	(require-any
-	(_g67 "")
+	(_g68 "")
 	(require-all
 		(subpath "/private/var/PersonaVolumes")
 		(require-any
-			(_g67 "")
+			(_g68 "")
 			(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/|$)")
 		)
 	)
 ))
-(define (_g69 _)
+(define (_g70 _)
 	(require-all
 	(extension-class "com.apple.StreamingUnzipService")
 	(signing-identifier "com.apple.appplaceholdersyncd")
 	(subpath "/private/var")
 	(extension "com.apple.sandbox.container")
-	(_g68 "")
-))
-(define (_g70 _)
-	(require-any
 	(_g69 "")
+))
+(define (_g71 _)
+	(require-any
+	(_g70 "")
 	(require-all
 		(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
 		(extension-class "com.apple.StreamingUnzipService")
 		(signing-identifier "com.apple.appplaceholdersyncd")
 		(subpath "/private/var")
 		(extension "com.apple.sandbox.container")
-		(_g68 "")
+		(_g69 "")
 	)
 	(require-all
 		(subpath "/private/var/containers/Shared/SystemGroup")
 		(require-any
-			(_g69 "")
+			(_g70 "")
 			(regex #"^/private/var/containers/Shared/SystemGroup/[^/]+(/|$)")
 		)
 	)
 ))
-(define (_g71 _)
+(define (_g72 _)
 	(require-all
 	(signing-identifier "com.apple.appplaceholdersyncd")
 	(subpath "/private/var")
 	(extension "com.apple.sandbox.container")
-	(_g68 "")
+	(_g69 "")
 ))
-(define (_g72 _)
-	(extension "com.apple.security.exception.files.home-relative-path.read-write"))
 (define (_g73 _)
+	(extension "com.apple.security.exception.files.home-relative-path.read-write"))
+(define (_g74 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read-write")
 	(require-any
-		(_g72 "")
+		(_g73 "")
 		(extension "com.apple.security.exception.files.absolute-path.read-write")
 	)
 ))
-(define (_g74 _)
+(define (_g75 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read-write")
 	(extension "com.apple.app-sandbox.read-write")
 ))
-(define (_g75 _)
-	(require-any
-	(_g74 "")
-	(extension "com.apple.clouddocs.version")
-))
 (define (_g76 _)
-	(require-all
-	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
 	(require-any
-		(_g74 "")
-		(require-all
-			(vnode-type REGULAR-FILE)
-			(_g75 "")
-		)
-	)
+	(_g75 "")
+	(extension "com.apple.clouddocs.version")
 ))
 (define (_g77 _)
 	(require-all
-	(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")
-	(vnode-type REGULAR-FILE)
-	(_g75 "")
+	(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
+	(require-any
+		(_g75 "")
+		(require-all
+			(vnode-type REGULAR-FILE)
+			(_g76 "")
+		)
+	)
 ))
 (define (_g78 _)
+	(require-all
+	(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")
+	(vnode-type REGULAR-FILE)
+	(_g76 "")
+))
+(define (_g79 _)
 	(require-all
 	(extension-class "com.apple.app-sandbox.read-write")
 	(extension "com.apple.app-sandbox.read-write")
 ))
-(define (_g79 _)
+(define (_g80 _)
 	(require-all
 	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 	(require-any

 		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 ))
-(define (_g80 _)
+(define (_g81 _)
 	(require-all
 	(subpath "/private/var/PersonaVolumes")
 	(require-any

 		(require-all
 			(subpath "${FRONT_USER_HOME}")
 			(require-any
-				(_g79 "")
+				(_g80 "")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 			)
 		)
 	)
 ))
-(define (_g81 _)
+(define (_g82 _)
 	(require-all
 	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 	(require-any

 		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 ))
-(define (_g82 _)
+(define (_g83 _)
 	(require-all
 	(subpath "${FRONT_USER_HOME}")
 	(require-any
-		(_g81 "")
+		(_g82 "")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 	)
 ))
-(define (_g83 _)
+(define (_g84 _)
 	(require-any
-	(_g82 "")
+	(_g83 "")
 	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 ))
-(define (_g84 _)
+(define (_g85 _)
 	(require-all
 	(subpath "/private/var")
 	(extension "com.apple.sandbox.application-group")

 		(require-all
 			(extension-class "com.apple.aned.read-only")
 			(require-any
-				(_g81 "")
 				(_g82 "")
+				(_g83 "")
 				(require-all
 					(subpath "/private/var/PersonaVolumes")
-					(_g83 "")
+					(_g84 "")
 				)
 			)
 		)
 		(require-all
 			(extension-class "com.apple.app-sandbox.read")
 			(subpath "/private/var/PersonaVolumes")
-			(_g83 "")
+			(_g84 "")
 		)
 		(require-all
 			(extension-class "com.apple.mediaserverd.read")
 			(subpath "/private/var/PersonaVolumes")
-			(_g83 "")
+			(_g84 "")
 		)
 	)
 ))
-(define (_g85 _)
-	(require-all
-	(subpath "${FRONT_USER_HOME}")
-	(require-any
-		(_g84 "")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-	)
-))
 (define (_g86 _)
 	(require-all
-	(extension-class "com.apple.mediaserverd.read")
+	(subpath "${FRONT_USER_HOME}")
 	(require-any
-		(_g81 "")
-		(require-all
-			(subpath "/private/var")
-			(require-any
-				(_g81 "")
-				(require-all
-					(extension "com.apple.sandbox.application-group")
-					(require-any
-						(_g84 "")
-						(_g85 "")
-						(require-all
-							(subpath "/private/var/PersonaVolumes")
-							(require-any
-								(_g85 "")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-						)
-					)
-				)
-			)
-		)
+		(_g85 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 	)
 ))
 (define (_g87 _)
 	(require-all
-	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+	(extension-class "com.apple.mediaserverd.read")
 	(require-any
+		(_g82 "")
 		(require-all
-			(%entitlement-is-present "com.apple.security.ts.tmpdir")
+			(subpath "/private/var")
 			(require-any
+				(_g82 "")
 				(require-all
-					(extension-class "com.apple.app-sandbox.read")
-					(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+					(extension "com.apple.sandbox.application-group")
 					(require-any
+						(_g85 "")
+						(_g86 "")
 						(require-all
-							(extension-class "com.apple.mediaserverd.read")
+							(subpath "/private/var/PersonaVolumes")
 							(require-any
-								(require-all
-									(extension "com.apple.security.exception.files.absolute-path.read-only")
-									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-								)
-								(require-all
-									(extension "com.apple.security.exception.files.absolute-path.read-write")
-									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-								)
-								(require-all
-									(extension "com.apple.security.exception.files.home-relative-path.read-only")
-									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-								)
-								(require-all
-									(extension "com.apple.security.exception.files.home-relative-path.read-write")
-									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
-								)
+								(_g86 "")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 							)
 						)
-						(require-any
-							(subpath "/private/var/factory_mount/[^/]+/Applications")
-							(subpath "/private/var/personalized_automation/Applications")
-							(subpath "/private/var/personalized_debug/Applications")
-							(subpath "/private/var/personalized_factory/[^/]+/Applications")
-						)
-						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-						(subpath "/AppleInternal/Applications")
-						(subpath "/Applications")
-						(subpath "/Developer/Applications")
-						(subpath "/System/Developer/Applications")
-						(subpath "/private/var/containers/Bundle")
 					)
 				)
-				(require-any
-					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-				)
 			)
 		)
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 ))
 (define (_g88 _)
 	(require-all
-	(subpath "${FRONT_USER_HOME}")
+	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 	(require-any
-		(_g87 "")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+		(require-all
+			(%entitlement-is-present "com.apple.security.ts.tmpdir")
+			(require-any
+				(require-all
+					(extension-class "com.apple.app-sandbox.read")
+					(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+					(require-any
+						(require-all
+							(extension-class "com.apple.mediaserverd.read")
+							(require-any
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.absolute-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-only")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+								(require-all
+									(extension "com.apple.security.exception.files.home-relative-path.read-write")
+									(%entitlement-is-bool-true "com.apple.security.ts.play-media")
+								)
+							)
+						)
+						(require-any
+							(subpath "/private/var/factory_mount/[^/]+/Applications")
+							(subpath "/private/var/personalized_automation/Applications")
+							(subpath "/private/var/personalized_debug/Applications")
+							(subpath "/private/var/personalized_factory/[^/]+/Applications")
+						)
+						(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+						(subpath "/AppleInternal/Applications")
+						(subpath "/Applications")
+						(subpath "/Developer/Applications")
+						(subpath "/System/Developer/Applications")
+						(subpath "/private/var/containers/Bundle")
+					)
+				)
+				(require-any
+					(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+				)
+			)
+		)
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 ))
 (define (_g89 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
 	(require-any
-	(_g88 "")
-	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+		(_g88 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
 ))
 (define (_g90 _)
+	(require-any
+	(_g89 "")
+	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+))
+(define (_g91 _)
 	(require-all
 	(subpath "/private/var")
 	(extension "com.apple.sandbox.application-group")

 		(require-all
 			(extension-class "com.apple.aned.read-only")
 			(require-any
-				(_g87 "")
 				(_g88 "")
+				(_g89 "")
 				(require-all
 					(subpath "/private/var/PersonaVolumes")
-					(_g89 "")
+					(_g90 "")
 				)
 			)
 		)
 		(require-all
 			(extension-class "com.apple.app-sandbox.read")
 			(subpath "/private/var/PersonaVolumes")
-			(_g89 "")
+			(_g90 "")
 		)
 		(require-all
 			(extension-class "com.apple.mediaserverd.read")
 			(subpath "/private/var/PersonaVolumes")
-			(_g89 "")
+			(_g90 "")
 		)
 	)
 ))
-(define (_g91 _)
-	(require-all
-	(subpath "${FRONT_USER_HOME}")
-	(require-any
-		(_g90 "")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-	)
-))
 (define (_g92 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(_g91 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g93 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read")
 	(require-any
-		(_g87 "")
+		(_g88 "")
 		(require-all
 			(subpath "/private/var")
 			(require-any
-				(_g87 "")
+				(_g88 "")
 				(require-all
 					(extension "com.apple.sandbox.application-group")
 					(require-any
-						(_g90 "")
 						(_g91 "")
+						(_g92 "")
 						(require-all
 							(subpath "/private/var/PersonaVolumes")
 							(require-any
-								(_g91 "")
+								(_g92 "")
 								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 							)
 						)

 		)
 	)
 ))
-(define (_g93 _)
+(define (_g94 _)
 	(require-all
 	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 	(require-any

 		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 ))
-(define (_g94 _)
+(define (_g95 _)
 	(require-all
 	(subpath "${FRONT_USER_HOME}")
 	(require-any
-		(_g93 "")
+		(_g94 "")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 	)
 ))
-(define (_g95 _)
+(define (_g96 _)
 	(require-any
-	(_g94 "")
+	(_g95 "")
 	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 ))
-(define (_g96 _)
+(define (_g97 _)
 	(require-all
 	(subpath "/private/var")
 	(extension "com.apple.sandbox.application-group")

 		(require-all
 			(extension-class "com.apple.aned.read-only")
 			(require-any
-				(_g93 "")
 				(_g94 "")
+				(_g95 "")
 				(require-all
 					(subpath "/private/var/PersonaVolumes")
-					(_g95 "")
+					(_g96 "")
 				)
 			)
 		)
 		(require-all
 			(extension-class "com.apple.app-sandbox.read")
 			(subpath "/private/var/PersonaVolumes")
-			(_g95 "")
+			(_g96 "")
 		)
 		(require-all
 			(extension-class "com.apple.mediaserverd.read")
 			(subpath "/private/var/PersonaVolumes")
-			(_g95 "")
+			(_g96 "")
 		)
 	)
 ))
-(define (_g97 _)
-	(require-all
-	(subpath "${FRONT_USER_HOME}")
-	(require-any
-		(_g96 "")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-	)
-))
 (define (_g98 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(_g97 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g99 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read")
 	(require-any
-		(_g93 "")
+		(_g94 "")
 		(require-all
 			(subpath "/private/var")
 			(require-any
-				(_g93 "")
+				(_g94 "")
 				(require-all
 					(extension "com.apple.sandbox.application-group")
 					(require-any
-						(_g96 "")
 						(_g97 "")
+						(_g98 "")
 						(require-all
 							(subpath "/private/var/PersonaVolumes")
 							(require-any
-								(_g97 "")
+								(_g98 "")
 								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 							)
 						)

 		)
 	)
 ))
-(define (_g99 _)
+(define (_g100 _)
 	(require-all
 	(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 	(require-any

 		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 ))
-(define (_g100 _)
+(define (_g101 _)
 	(require-all
 	(subpath "${FRONT_USER_HOME}")
 	(require-any
-		(_g99 "")
+		(_g100 "")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
 	)
 ))
-(define (_g101 _)
+(define (_g102 _)
 	(require-any
-	(_g100 "")
+	(_g101 "")
 	(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 ))
-(define (_g102 _)
+(define (_g103 _)
 	(require-all
 	(subpath "/private/var")
 	(extension "com.apple.sandbox.application-group")

 			(extension-class "com.apple.aned.read-only")
 			(require-any
 				(_g100 "")
-				(_g99 "")
+				(_g101 "")
 				(require-all
 					(subpath "/private/var/PersonaVolumes")
-					(_g101 "")
+					(_g102 "")
 				)
 			)
 		)
 		(require-all
 			(extension-class "com.apple.app-sandbox.read")
 			(subpath "/private/var/PersonaVolumes")
-			(_g101 "")
+			(_g102 "")
 		)
 		(require-all
 			(extension-class "com.apple.mediaserverd.read")
 			(subpath "/private/var/PersonaVolumes")
-			(_g101 "")
+			(_g102 "")
 		)
 	)
 ))
-(define (_g103 _)
-	(require-all
-	(subpath "${FRONT_USER_HOME}")
-	(require-any
-		(_g102 "")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-	)
-))
 (define (_g104 _)
+	(require-all
+	(subpath "${FRONT_USER_HOME}")
+	(require-any
+		(_g103 "")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+	)
+))
+(define (_g105 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read")
 	(require-any
-		(_g99 "")
+		(_g100 "")
 		(require-all
 			(subpath "/private/var")
 			(require-any
-				(_g99 "")
+				(_g100 "")
 				(require-all
 					(extension "com.apple.sandbox.application-group")
 					(require-any
-						(_g102 "")
 						(_g103 "")
+						(_g104 "")
 						(require-all
 							(subpath "/private/var/PersonaVolumes")
 							(require-any
-								(_g103 "")
+								(_g104 "")
 								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
 							)
 						)

 		)
 	)
 ))
-(define (_g105 _)
+(define (_g106 _)
 	(require-all
 	(extension "com.apple.security.exception.files.home-relative-path.read-write")
 	(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 ))
-(define (_g106 _)
+(define (_g107 _)
 	(require-all
 	(extension-class "com.apple.mediaserverd.read")
 	(require-any
-		(_g105 "")
+		(_g106 "")
 		(require-all
 			(extension "com.apple.security.exception.files.absolute-path.read-only")
 			(%entitlement-is-bool-true "com.apple.security.ts.play-media")

 		)
 	)
 ))
-(define (_g107 _)
+(define (_g108 _)
 	(require-any
-	(_g106 "")
+	(_g107 "")
 	(require-any
 		(subpath "/private/var/factory_mount/[^/]+/Applications")
 		(subpath "/private/var/personalized_automation/Applications")

 	(subpath "/System/Developer/Applications")
 	(subpath "/private/var/containers/Bundle")
 ))
-(define (_g108 _)
+(define (_g109 _)
 	(require-all
 	(extension-class "com.apple.app-sandbox.read")
 	(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-	(_g107 "")
+	(_g108 "")
 ))
-(define (_g109 _)
+(define (_g110 _)
 	(require-all
 	(%entitlement-is-present "com.apple.security.ts.tmpdir")
 	(require-any
-		(_g108 "")
+		(_g109 "")
 		(require-any
 			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
 			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
 		)
 	)
 ))
-(define (_g110 _)
+(define (_g111 _)
 	(require-all
 	(extension-class "com.apple.aned.read-only")
 	(%entitlement-is-bool-true "com.apple.security.ts.asset-access")

 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any
-			(_g73 "")
-			(_g78 "")
+			(_g74 "")
+			(_g79 "")
 			(require-all
 				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")

 			(require-all
 				(extension "com.apple.librarian.ubiquity-container")
 				(require-any
-					(_g73 "")
+					(_g74 "")
 					(require-all
 						(subpath "${HOME}/Library/Mobile Documents")
 						(extension-class "com.apple.mediaserverd.read-write")

 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g73 "")
+							(_g74 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
 								(require-any
-									(_g73 "")
+									(_g74 "")
 									(require-all
 										(subpath "${FRONT_USER_HOME}")
 										(require-any

 			(require-all
 				(extension-class "com.apple.mediaserverd.read")
 				(require-any
-					(_g72 "")
+					(_g73 "")
 					(extension "com.apple.app-sandbox.read-write")
 					(extension "com.apple.security.exception.files.absolute-path.read-only")
 					(extension "com.apple.security.exception.files.absolute-path.read-write")

 			(require-all
 				(extension-class "com.apple.quicklook.readonly")
 				(require-any
-					(_g74 "")
-					(_g76 "")
+					(_g75 "")
 					(_g77 "")
 					(_g78 "")
+					(_g79 "")
 					(require-all
 						(extension-class "com.apple.mediaserverd.read")
 						(extension "com.apple.app-sandbox.read-write")

 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g77 "")
+							(_g78 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
 								(require-any
-									(_g76 "")
+									(_g77 "")
 									(require-all
 										(require-any
 											(subpath "${FRONT_USER_HOME}")

 	(require-all
 		(extension-class "com.apple.StreamingUnzipService")
 		(require-any
-			(_g49 "")
+			(_g50 "")
 			(require-all
 				(signing-identifier "com.apple.assistantd")
 				(require-any
-					(_g49 "")
+					(_g50 "")
 					(subpath "${HOME}/Library/Caches/VoiceTrigger")
 				)
 			)

 	(require-all
 		(extension-class "com.apple.StreamingUnzipService")
 		(require-any
-			(_g71 "")
+			(_g72 "")
 			(require-all
 				(extension "com.apple.sandbox.system-group")
 				(require-any
-					(_g71 "")
+					(_g72 "")
 					(require-all
 						(%entitlement-is-present "com.apple.security.system-group-containers")
 						(signing-identifier "com.apple.bookassetd")
-						(_g70 "")
+						(_g71 "")
 					)
 					(require-all
 						(%entitlement-is-present "com.apple.security.system-groups")
 						(require-any
-							(_g69 "")
+							(_g70 "")
 							(require-all
 								(signing-identifier "com.apple.bookassetd")
-								(_g70 "")
+								(_g71 "")
 							)
 						)
 					)

 			(require-all
 				(signing-identifier "com.apple.assistantd")
 				(require-any
-					(_g17 "")
+					(_g18 "")
 					(subpath "${HOME}/Library/Caches/VoiceTrigger")
 				)
 			)
 			(require-all
 				(subpath "${HOME}/Library/VoiceTrigger")
 				(require-any
-					(_g17 "")
+					(_g18 "")
 					(signing-identifier "com.apple.corespeechd")
 				)
 			)

 	(require-all
 		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(_g108 "")
 			(_g109 "")
+			(_g110 "")
 			(require-all
 				(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
 				(require-any
-					(_g109 "")
+					(_g110 "")
 					(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 				)
 			)
 			(require-all
 				(extension-class "com.apple.aned.read-only")
 				(require-any
-					(_g106 "")
+					(_g107 "")
 					(require-all
 						(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-						(_g107 "")
+						(_g108 "")
 					)
 				)
 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read")
 				(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-				(_g107 "")
+				(_g108 "")
 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read-write")
 				(require-any
-					(_g105 "")
+					(_g106 "")
 					(require-all
 						(extension "com.apple.security.exception.files.absolute-path.read-write")
 						(%entitlement-is-bool-true "com.apple.security.ts.play-media")

 	(require-all
 		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(_g44 "")
+			(_g45 "")
 			(require-all
 				(signing-identifier "com.apple.anomalydetectiond")
 				(require-any
-					(_g44 "")
+					(_g45 "")
 					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
 				)
 			)

 	(require-all
 		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(_g60 "")
 			(_g61 "")
+			(_g62 "")
 			(require-all
 				(extension-class "com.apple.aned.read-only")
 				(require-any
-					(_g58 "")
-					(_g64 "")
+					(_g59 "")
+					(_g65 "")
 					(require-all
 						(extension-class "com.apple.app-sandbox.read")
 						(require-any
-							(_g62 "")
-							(_g64 "")
+							(_g63 "")
+							(_g65 "")
 							(require-all
 								(extension-class "com.apple.mediaserverd.read")
 								(signing-identifier "com.apple.linkd")
-								(_g55 "")
+								(_g56 "")
 							)
 							(require-all
 								(signing-identifier "com.apple.mediaplaybackd")
-								(_g63 "")
+								(_g64 "")
 							)
 						)
 					)
 					(require-all
 						(extension-class "com.apple.app-sandbox.read-write")
 						(signing-identifier "com.apple.mediaplaybackd")
-						(_g63 "")
+						(_g64 "")
 					)
 					(require-all
 						(extension-class "com.apple.mediaserverd.read")
 						(require-any
-							(_g56 "")
+							(_g57 "")
 							(require-all
 								(extension-class "com.apple.mediaserverd.read-write")
 								(signing-identifier "com.apple.mediaplaybackd")
-								(_g63 "")
+								(_g64 "")
 							)
 							(require-all
 								(signing-identifier "com.apple.mediaplaybackd")
-								(_g57 "")
+								(_g58 "")
 							)
 						)
 					)
 					(require-all
 						(signing-identifier "com.apple.momentsd")
-						(_g59 "")
+						(_g60 "")
 					)
 				)
 			)
 			(require-all
 				(extension-class "com.apple.app-sandbox.read")
 				(signing-identifier "com.apple.momentsd")
-				(_g59 "")
+				(_g60 "")
 			)
 			(require-all
 				(extension-class "com.apple.mediaserverd.read")
 				(signing-identifier "com.apple.momentsd")
-				(_g59 "")
+				(_g60 "")
 			)
 			(require-all
 				(signing-identifier "com.apple.momentsd")
 				(require-any
-					(_g61 "")
+					(_g62 "")
 					(require-all
 						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
 						(require-any
-							(_g60 "")
+							(_g61 "")
 							(extension-class "com.apple.mediaserverd.read")
 							(extension-class "com.apple.mediaserverd.read-write")
 						)

 	(require-all
 		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(_g79 "")
+			(_g80 "")
 			(require-all
 				(extension "com.apple.sandbox.application-group")
 				(require-any
-					(_g79 "")
+					(_g80 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g80 "")
+							(_g81 "")
 							(require-all
 								(subpath "${FRONT_USER_HOME}")
 								(require-any
-									(_g80 "")
+									(_g81 "")
 									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 								)
 							)

 			)
 		)
 	)
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-				(signing-identifier "com.apple.fileindexerd")
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-				(signing-identifier "com.apple.fileindexerd")
-			)
-		)
-	)
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
 		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")

 		(extension-class "com.apple.app-sandbox.read")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(_g98 "")
+			(_g99 "")
 			(require-all
 				(subpath "/private/var")
 				(require-any
-					(_g98 "")
+					(_g99 "")
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 						(require-any
-							(_g98 "")
+							(_g99 "")
 							(subpath "${FRONT_USER_HOME}")
 						)
 					)

 			(require-all
 				(extension-class "com.apple.app-sandbox.read-write")
 				(require-any
-					(_g33 "")
+					(_g34 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g33 "")
+							(_g34 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 								(require-any

 									(require-all
 										(signing-identifier "com.apple.mediaplaybackd")
 										(require-any
-											(_g29 "")
-											(_g31 "")
+											(_g30 "")
+											(_g32 "")
 											(require-all
 												(require-any
 													(subpath "${FRONT_USER_HOME}")
 													(subpath "${HOME}")
 												)
 												(require-any
-													(_g31 "")
+													(_g32 "")
 													(require-all
 														(subpath "/private/var")
 														(require-any
-															(_g31 "")
+															(_g32 "")
 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 														)
 													)

 			(require-all
 				(extension-class "com.apple.mediaserverd.read-write")
 				(signing-identifier "com.apple.momentsd")
-				(_g52 "")
+				(_g53 "")
 			)
 			(require-all
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 					(require-all
 						(extension-class "com.apple.app-sandbox.read-write")
 						(signing-identifier "com.apple.momentsd")
-						(_g52 "")
+						(_g53 "")
 					)
 				)
 			)

 			)
 		)
 	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		(signing-identifier "com.apple.fileindexerd")
-	)
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
 		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")

 		(extension-class "com.apple.app-sandbox.read-write")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(_g92 "")
+			(_g93 "")
 			(require-all
 				(subpath "/private/var")
 				(require-any
-					(_g92 "")
+					(_g93 "")
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 						(require-any
-							(_g92 "")
+							(_g93 "")
 							(subpath "${FRONT_USER_HOME}")
 						)
 					)

 			(require-all
 				(extension-class "com.apple.app-sandbox.read-write")
 				(require-any
-					(_g28 "")
+					(_g29 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g28 "")
+							(_g29 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 								(require-any

 									(require-all
 										(signing-identifier "com.apple.mediaplaybackd")
 										(require-any
-											(_g24 "")
-											(_g26 "")
+											(_g25 "")
+											(_g27 "")
 											(require-all
 												(require-any
 													(subpath "${FRONT_USER_HOME}")
 													(subpath "${HOME}")
 												)
 												(require-any
-													(_g26 "")
+													(_g27 "")
 													(require-all
 														(subpath "/private/var")
 														(require-any
-															(_g26 "")
+															(_g27 "")
 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 														)
 													)

 			(require-all
 				(extension-class "com.apple.mediaserverd.read-write")
 				(signing-identifier "com.apple.momentsd")
-				(_g51 "")
+				(_g52 "")
 			)
 			(require-all
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 					(require-all
 						(extension-class "com.apple.app-sandbox.read-write")
 						(signing-identifier "com.apple.momentsd")
-						(_g51 "")
+						(_g52 "")
 					)
 				)
 			)
 			(subpath "${HOME}/Library/com.apple.momentsd")
 		)
 	)
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		(signing-identifier "com.apple.fileindexerd")
-	)
 	(require-all
 		(extension-class "com.apple.corespotlightservice.read-write")
 		(signing-identifier "com.apple.health.records")

 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any
-			(_g102 "")
-			(_g104 "")
+			(_g103 "")
+			(_g105 "")
 			(require-all
 				(extension "com.apple.sandbox.application-group")
 				(require-any
-					(_g104 "")
+					(_g105 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g104 "")
+							(_g105 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 								(require-any
-									(_g104 "")
+									(_g105 "")
 									(subpath "${FRONT_USER_HOME}")
 								)
 							)

 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
 		(require-any
-			(_g66 "")
+			(_g67 "")
 			(require-all
 				(extension-class "com.apple.mediaserverd.read-write")
 				(signing-identifier "com.apple.avconferenced")

 			(require-all
 				(signing-identifier "com.apple.cameracaptured")
 				(require-any
-					(_g66 "")
+					(_g67 "")
 					(extension "com.apple.mediaserverd.read-write")
 				)
 			)

 			(require-all
 				(extension-class "com.apple.app-sandbox.read-write")
 				(require-any
-					(_g38 "")
+					(_g39 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g38 "")
+							(_g39 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 								(require-any

 									(require-all
 										(signing-identifier "com.apple.mediaplaybackd")
 										(require-any
-											(_g34 "")
-											(_g36 "")
+											(_g35 "")
+											(_g37 "")
 											(require-all
 												(require-any
 													(subpath "${FRONT_USER_HOME}")
 													(subpath "${HOME}")
 												)
 												(require-any
-													(_g36 "")
+													(_g37 "")
 													(require-all
 														(subpath "/private/var")
 														(require-any
-															(_g36 "")
+															(_g37 "")
 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 														)
 													)

 			(require-all
 				(extension-class "com.apple.mediaserverd.read-write")
 				(signing-identifier "com.apple.momentsd")
-				(_g53 "")
+				(_g54 "")
 			)
 			(require-all
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 					(require-all
 						(extension-class "com.apple.app-sandbox.read-write")
 						(signing-identifier "com.apple.momentsd")
-						(_g53 "")
+						(_g54 "")
 					)
 				)
 			)
 			(subpath "${HOME}/Library/com.apple.momentsd")
 		)
 	)
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		(signing-identifier "com.apple.fileindexerd")
-	)
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
 		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")

 		(extension-class "com.apple.mediaserverd.read-write")
 		(extension "com.apple.sandbox.application-group")
 		(require-any
-			(_g86 "")
+			(_g87 "")
 			(require-all
 				(subpath "/private/var")
 				(require-any
-					(_g86 "")
+					(_g87 "")
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
 						(require-any
-							(_g86 "")
+							(_g87 "")
 							(subpath "${FRONT_USER_HOME}")
 						)
 					)

 			(require-all
 				(extension-class "com.apple.app-sandbox.read-write")
 				(require-any
-					(_g23 "")
+					(_g24 "")
 					(require-all
 						(subpath "/private/var")
 						(require-any
-							(_g23 "")
+							(_g24 "")
 							(require-all
 								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader/recompiled(/|$)")
 								(require-any

 									(require-all
 										(signing-identifier "com.apple.mediaplaybackd")
 										(require-any
-											(_g19 "")
-											(_g21 "")
+											(_g20 "")
+											(_g22 "")
 											(require-all
 												(require-any
 													(subpath "${FRONT_USER_HOME}")
 													(subpath "${HOME}")
 												)
 												(require-any
-													(_g21 "")
+													(_g22 "")
 													(require-all
 														(subpath "/private/var")
 														(require-any
-															(_g21 "")
+															(_g22 "")
 															(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
 														)
 													)

 			(require-all
 				(extension-class "com.apple.mediaserverd.read-write")
 				(signing-identifier "com.apple.momentsd")
-				(_g50 "")
+				(_g51 "")
 			)
 			(require-all
 				(subpath "${HOME}/Library/Caches/com.apple.momentsd")

 					(require-all
 						(extension-class "com.apple.app-sandbox.read-write")
 						(signing-identifier "com.apple.momentsd")
-						(_g50 "")
+						(_g51 "")
 					)
 				)
 			)
 			(subpath "${HOME}/Library/com.apple.momentsd")
 		)
 	)
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		(signing-identifier "com.apple.fileindexerd")
-	)
 	(require-all
 		(extension-class "com.apple.nsurlsessiond.readonly")
 		(extension "com.apple.sandbox.application-group")

 	(require-all
 		(extension-class "com.apple.spotlight-indexable")
 		(require-any
-			(_g65 "")
+			(_g13 "")
 			(require-all
+				(signing-identifier "com.apple.intelligenceflow.intelligenceflowd")
 				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
+					(_g13 "")
+					(extension "com.apple.app-sandbox.read")
 				)
+			)
+		)
+	)
+	(require-all
+		(extension-class "com.apple.spotlight-indexable")
+		(require-any
+			(_g66 "")
+			(require-all
+				(subpath "/private/var")
 				(require-any
-					(_g65 "")
+					(_g66 "")
 					(require-all
-						(subpath "/private/var")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
 						(require-any
-							(_g65 "")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-								(signing-identifier "com.apple.fileindexerd")
-							)
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
 						)
+						(signing-identifier "com.apple.fileindexerd")
 					)
 				)
 			)

 	(require-all
 		(extension-class "com.apple.usernotifications.attachments.read-only")
 		(require-any
-			(_g18 "")
+			(_g19 "")
 			(require-all
 				(subpath "/private/var")
 				(require-any
-					(_g18 "")
+					(_g19 "")
 					(require-all
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")
 						(subpath "${HOME}")

 			)
 		)
 	)
+	(require-all
+		(signing-identifier "com.apple.filederivatived")
+		(extension "com.apple.spotlight-indexable")
+		(extension-class "com.apple.app-sandbox.read")
+	)
+	(require-all
+		(signing-identifier "com.apple.fileindexerd")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+				(require-any
+					(extension-class "com.apple.aned.read-only")
+					(extension-class "com.apple.app-sandbox.read")
+					(extension-class "com.apple.app-sandbox.read-write")
+					(extension-class "com.apple.mediaserverd.read")
+					(extension-class "com.apple.mediaserverd.read-write")
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+				(extension-class "com.apple.mediaserverd.read-write")
+			)
+		)
+	)
 	(require-all
 		(signing-identifier "com.apple.geoanalyticsd")
 		(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")

 	(require-all
 		(subpath "${HOME}/Library/Assets")
 		(require-any
-			(_g110 "")
+			(_g111 "")
 			(require-all
 				(extension-class "com.apple.mediaserverd.read")
 				(extension "com.apple.assets.read")
 				(require-any
 					(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-					(_g110 "")
+					(_g111 "")
 				)
 			)
 		)

 
 (allow file-read*
 	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
-	)
-)
-(allow file-read*
-	(require-any
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.videocodecd")
 	)
 )
 (allow file-read*
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")
+		(signing-identifier "com.apple.wapic")
 		(require-any
-			(require-any
-				(literal "/usr/standalone/firmware/apticket.der")
-				(subpath "/private/var/hardware/FactoryData")
-			)
-			(subpath "/private/preboot")
+			(literal "/dev/bpf[0-9]")
+			(regex #"/dev/bpf([0-9])+")
 		)
 	)
 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
-		(vnode-type REGULAR-FILE)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var/containers/Data/System/com.apple.geod")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")
-		(vnode-type REGULAR-FILE)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read*
-	(require-all
-		(system-attribute carrier-build internal-build)
-		(signing-identifier "com.apple.audiomxd")
-		(require-any
-			(literal ".caf")
-			(literal ".wav")
-			(literal ".wave")
-		)
-		(require-any
-			(subpath "${FRONT_USER_HOME}/tmp")
-			(subpath "/private/var/tmp")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-		(process-attribute is-apple-signed-executable)
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read*
-	(require-all
-		(vnode-type DIRECTORY)
-		(require-any
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}/Library/AddressBook")
-					(subpath "${FRONT_USER_HOME}/Library/Contacts")
-					(subpath "${FRONT_USER_HOME}/Library/Health")
-					(subpath "${FRONT_USER_HOME}/Library/Mail")
-					(subpath "${FRONT_USER_HOME}/Library/NanoMailKit")
-					(subpath "${FRONT_USER_HOME}/Library/NanoPhotos")
-					(subpath "${FRONT_USER_HOME}/Library/Passes")
-					(subpath "${FRONT_USER_HOME}/Library/Recordings")
-					(subpath "${FRONT_USER_HOME}/Library/Reminders")
-					(subpath "${FRONT_USER_HOME}/Library/SMS")
-					(subpath "${FRONT_USER_HOME}/Library/Safari")
-					(subpath "${FRONT_USER_HOME}/Media/Books")
-					(subpath "${FRONT_USER_HOME}/Media/Downloads")
-					(subpath "${FRONT_USER_HOME}/Media/Recordings")
-					(subpath "${FRONT_USER_HOME}/Media/iTunes_Control")
-				)
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}/Library/Notes")
-					(subpath "${FRONT_USER_HOME}/Library/Voicemail")
-				)
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}/Library/Logs")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "${PROCESS_TEMP_DIR}/powerlog")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.storagedatad")
-							)
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.storagedatad")
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(require-all
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-										(signing-identifier "com.apple.storagedatad")
-									)
-									(require-all
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-										(signing-identifier "com.apple.storagedatad")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "${HOME}")
-						(require-any
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.storagedatad")
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(require-all
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-										(signing-identifier "com.apple.storagedatad")
-									)
-									(require-all
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-										(signing-identifier "com.apple.storagedatad")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.storagedatad")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.storagedatad")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/log")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "/private/var/logs")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "/private/var/tmp/powerlog")
-				(signing-identifier "com.apple.storagedatad")
-			)
-			(require-all
-				(subpath "/private/var/wireless/Library/Logs")
-				(signing-identifier "com.apple.storagedatad")
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(system-attribute developer-mode)
-		(literal "/mach.*")
-		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
-		(require-any
-			(require-any
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
-			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/AppleInternal/Applications")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/System/Developer/Applications")
-			(subpath "/private/var/containers/Bundle")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/System/Library/Carrier Bundles")
-		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
-		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
-		(extension "com.apple.identityservices.deliver")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(require-any
-			(require-all
-				(subpath "/System/Library/Carrier Bundles")
-				(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-			)
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-						(require-any
-							(require-all
-								(subpath "/System/Library/Carrier Bundles")
-								(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-							)
-							(subpath "${FRONT_USER_HOME}")
-						)
-					)
-					(require-all
-						(subpath "/System/Library/Carrier Bundles")
-						(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(subpath "${HOME}/Library/Fonts")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			)
-			(require-all
-				(extension "com.apple.librarian.ubiquity-container")
-				(require-any
-					(require-all
-						(subpath "/private/var")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-						(subpath "${FRONT_USER_HOME}")
-					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				)
-			)
-			(require-all
-				(require-any
-					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
-					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-					(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-				)
-				(require-any
-					(extension "com.apple.librarian.ubiquity-revision")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 		(literal "/private/var/preferences/com.apple.security.plist")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container-proxy")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
-		(literal "${FRONT_USER_HOME}")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-				(extension "com.apple.tcc.kTCCServiceAddressBook")
-				(require-any
-					(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
-					(subpath "${HOME}/Library/AddressBook")
-					(subpath "${HOME}/Library/AddressBook/Delegates")
-				)
-			)
-			(subpath "${HOME}/Library/Fonts")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(extension "com.apple.mediaserverd.read-write")
-		(signing-identifier "com.apple.audiomxd")
-	)
-)
-(allow file-read*
-	(require-all
-		(extension "com.apple.mediaserverd.read")
-		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.fileindexerd")
-		(require-any
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.linkd")
-		(require-any
-			(require-any
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
-			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/AppleInternal/Applications")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/System/Developer/Applications")
-			(subpath "/private/var/containers/Bundle")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/AppleInternal")
-		(system-attribute carrier-build)
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.airplayd")
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.geoanalyticsd")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-				)
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.network.client")
-		(require-any
-			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
-			(literal "/private/var/db/com.apple.networkextension.tracker-info")
-			(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
-			(literal "/private/var/preferences/com.apple.networkd.plist")
-			(literal "/private/var/preferences/com.apple.security.plist")
-			(require-all
-				(%entitlement-is-present "com.apple.private.networkextension.configuration")
-				(literal "/private/var/preferences/com.apple.networkextension.plist")
-			)
-			(require-all
-				(process-attribute is-apple-signed-executable)
-				(require-any
-					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.cameracaptured")
-		(require-any
-			(extension "com.apple.mediaserverd.read")
-			(extension "com.apple.mediaserverd.read-write")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-		)
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-read*
-	(require-all
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
-		)
-		(signing-identifier "com.apple.MTLAssetUpgraderD")
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.cloudpaird")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
-		(require-any
-			(extension "com.apple.sandbox.application-group")
-			(require-all
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.mediaplaybackd")
-		(require-any
-			(extension "com.apple.mediaserverd.read")
-			(extension "com.apple.mediaserverd.read-write")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.gpsd")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.announced")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
-			(subpath "/private/var/tmp/com.apple.announced")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.manageddeviced")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-								)
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-					)
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.anomalydetectiond")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-				)
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.siriknowledged")
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.momentsd")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(require-any
-					(require-any
-						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-						(subpath "${HOME}/Library/com.apple.momentsd")
-					)
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
-				)
-			)
-			(require-any
-				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
-				(subpath "${HOME}/Library/com.apple.momentsd")
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.security.KeychainDBMover")
-		(subpath "${FRONT_USER_HOME}/Library/Keychains")
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/db/com.apple.networkextension.tracker-info")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments(/|$)")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-		)
+		(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
 (allow file-read*

 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(signing-identifier "com.apple.managedappdistributiond")
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-				)
-			)
-			(require-all
-				(signing-identifier "com.apple.storekitd")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/Applications")
+		(subpath "/AppleInternal/Applications")
 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
 (allow file-read*
 	(require-all
-		(signing-identifier "com.apple.privacyaccountingctl")
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.mediaplaybackd")
 	)
 )
 (allow file-read*
 	(require-all
-		(signing-identifier "com.apple.wapic")
-		(require-any
-			(literal "/dev/bpf[0-9]")
-			(regex #"/dev/bpf([0-9])+")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.mDNSResponderHelper")
-		(require-any
-			(literal "/dev/bpf[0-9]")
-			(regex #"/dev/bpf([0-9])+")
-		)
+		(subpath "/System/Developer/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
 (allow file-read*

 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
-(allow file-read*
-	(require-all
-		(subpath "/AppleInternal/Applications")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-			)
-			(require-any
-				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.storagedatad")
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.tursd")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-			)
-			(require-any
-				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/Developer/Applications")
-		(require-any
-			(signing-identifier "com.apple.managedappdistributiond")
-			(signing-identifier "com.apple.storekitd")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.videocodecd")
-	)
-)
-(allow file-read*
-	(require-all
-		(signing-identifier "com.apple.audiomxd")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read*
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-							(subpath "${FRONT_USER_HOME}")
-						)
-					)
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-					)
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/preferences/com.apple.security.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
-	)
-)
-(allow file-read*
-	(require-all
-		(extension "com.apple.assets.read")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
-				(subpath "/private/var/MobileAsset")
-			)
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
-				(require-any
-					(subpath "${HOME}/Library/Assets")
-					(subpath "/private/var/MobileAsset")
-				)
-			)
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(uid 0)
-		(vnode-type CHARACTER-DEVICE)
-		(%entitlement-is-bool-true "com.apple.security.ts.bpf")
-		(literal "/dev/bpf*")
-	)
-)
-(allow file-read*
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.tmpdir")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
-		)
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-		(subpath "${FRONT_USER_HOME}")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
-		(subpath "${FRONT_USER_HOME}")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
 (allow file-read*
 	(require-all
 		(subpath "/private/var/containers/Bundle")

 )
 (allow file-read*
 	(require-all
-		(subpath "/System/Developer/Applications")
+		(subpath "/Applications")
 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
 (allow file-read*
 	(require-all
 		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
+		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
+		(signing-identifier "com.apple.chronod")
 	)
 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
+		(signing-identifier "com.apple.cloudpaird")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
 	)
 )
 (allow file-read*

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container-proxy")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.privacyaccountingctl")
+		(literal "/dev/ttys*")
+		(regex #"^/dev/ttys([0-9])*")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/Developer/Applications")
+		(require-any
+			(signing-identifier "com.apple.managedappdistributiond")
+			(signing-identifier "com.apple.storekitd")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.announced")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
+			(subpath "/private/var/tmp/com.apple.announced")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.security.KeychainDBMover")
+		(subpath "${FRONT_USER_HOME}/Library/Keychains")
+	)
+)
+(allow file-read*
+	(require-all
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
+		)
+		(signing-identifier "com.apple.MTLAssetUpgraderD")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
+		(extension "com.apple.identityservices.deliver")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.gpsd")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.mDNSResponderHelper")
+		(require-any
+			(literal "/dev/bpf[0-9]")
+			(regex #"/dev/bpf([0-9])+")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.network.client")
+		(require-any
+			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+			(literal "/private/var/db/com.apple.networkextension.tracker-info")
+			(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+			(literal "/private/var/preferences/com.apple.networkd.plist")
+			(literal "/private/var/preferences/com.apple.security.plist")
+			(require-all
+				(%entitlement-is-present "com.apple.private.networkextension.configuration")
+				(literal "/private/var/preferences/com.apple.networkextension.plist")
+			)
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(require-any
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.airplayd")
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+						(require-any
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.audiomxd")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.mediaserverd.read")
+		(require-any
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.audiomxd")
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.filederivatived")
+		(extension "com.apple.spotlight-indexable")
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.siriknowledged")
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+		(require-any
+			(require-any
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
+			(subpath "/private/var/containers/Bundle")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+		(subpath "${FRONT_USER_HOME}")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/System/Library/Carrier Bundles")
+		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(subpath "${HOME}/Library/Fonts")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.tmpdir")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")
+		(require-any
+			(require-any
+				(literal "/usr/standalone/firmware/apticket.der")
+				(subpath "/private/var/hardware/FactoryData")
+			)
+			(subpath "/private/preboot")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
+		(literal "/private/var/preferences/com.apple.security.plist")
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/db/com.apple.networkextension.tracker-info")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(require-any
+			(require-all
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			)
+			(require-all
+				(extension "com.apple.librarian.ubiquity-container")
+				(require-any
+					(require-all
+						(subpath "/private/var")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+						(subpath "${FRONT_USER_HOME}")
+					)
+					(subpath "${HOME}/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+				)
+			)
+			(require-all
+				(require-any
+					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
+					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+					(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+				)
+				(require-any
+					(extension "com.apple.librarian.ubiquity-revision")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
+		(literal "${FRONT_USER_HOME}")
+	)
+)
+(allow file-read*
+	(require-all
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var/containers/Data/System/com.apple.geod")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(system-attribute developer-mode)
+		(literal "/mach.*")
+		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(require-any
+			(require-all
+				(subpath "/System/Library/Carrier Bundles")
+				(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+						(require-any
+							(require-all
+								(subpath "/System/Library/Carrier Bundles")
+								(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+							)
+							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+					(require-all
+						(subpath "/System/Library/Carrier Bundles")
+						(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/usr/local/lib")
+		(system-attribute carrier-build)
+	)
+)
+(allow file-read*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(require-any
+			(require-all
+				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+				(extension "com.apple.tcc.kTCCServiceAddressBook")
+				(require-any
+					(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
+					(subpath "${HOME}/Library/AddressBook")
+					(subpath "${HOME}/Library/AddressBook/Delegates")
+				)
+			)
+			(subpath "${HOME}/Library/Fonts")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+		(process-attribute is-apple-signed-executable)
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")
+		(vnode-type REGULAR-FILE)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
+		(subpath "${FRONT_USER_HOME}")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.assets.read")
+		(require-any
+			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
+				(subpath "/private/var/MobileAsset")
+			)
+			(require-all
+				(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
+				(require-any
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(uid 0)
+		(vnode-type CHARACTER-DEVICE)
+		(%entitlement-is-bool-true "com.apple.security.ts.bpf")
+		(literal "/dev/bpf*")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
+		(vnode-type REGULAR-FILE)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/AppleInternal")
+		(system-attribute carrier-build)
+	)
+)
+(allow file-read*
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.geoanalyticsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.fileindexerd")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.linkd")
+		(require-any
+			(require-any
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
+			(subpath "/private/var/containers/Bundle")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.cameracaptured")
+		(require-any
+			(extension "com.apple.mediaserverd.read")
+			(extension "com.apple.mediaserverd.read-write")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read")
+			(extension "com.apple.mediaserverd.read-write")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.storagedatad")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.tursd")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.anomalydetectiond")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(signing-identifier "com.apple.managedappdistributiond")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+				)
+			)
+			(require-all
+				(signing-identifier "com.apple.storekitd")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
+		(require-any
+			(extension "com.apple.sandbox.application-group")
+			(require-all
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments(/|$)")
+						(signing-identifier "com.apple.storagedatad")
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.nanophoned")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(vnode-type DIRECTORY)
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}/Library/AddressBook")
+					(subpath "${FRONT_USER_HOME}/Library/Contacts")
+					(subpath "${FRONT_USER_HOME}/Library/Health")
+					(subpath "${FRONT_USER_HOME}/Library/Mail")
+					(subpath "${FRONT_USER_HOME}/Library/NanoMailKit")
+					(subpath "${FRONT_USER_HOME}/Library/NanoPhotos")
+					(subpath "${FRONT_USER_HOME}/Library/Passes")
+					(subpath "${FRONT_USER_HOME}/Library/Recordings")
+					(subpath "${FRONT_USER_HOME}/Library/Reminders")
+					(subpath "${FRONT_USER_HOME}/Library/SMS")
+					(subpath "${FRONT_USER_HOME}/Library/Safari")
+					(subpath "${FRONT_USER_HOME}/Media/Books")
+					(subpath "${FRONT_USER_HOME}/Media/Downloads")
+					(subpath "${FRONT_USER_HOME}/Media/Recordings")
+					(subpath "${FRONT_USER_HOME}/Media/iTunes_Control")
+				)
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}/Library/Notes")
+					(subpath "${FRONT_USER_HOME}/Library/Voicemail")
+				)
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}/Library/Logs")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "${PROCESS_TEMP_DIR}/powerlog")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(subpath "${HOME}")
+						(require-any
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+									(require-all
+										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+										(signing-identifier "com.apple.storagedatad")
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.storagedatad")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/log")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "/private/var/logs")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "/private/var/tmp/powerlog")
+				(signing-identifier "com.apple.storagedatad")
+			)
+			(require-all
+				(subpath "/private/var/wireless/Library/Logs")
+				(signing-identifier "com.apple.storagedatad")
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(system-attribute carrier-build internal-build)
+		(signing-identifier "com.apple.audiomxd")
+		(require-any
+			(literal ".caf")
+			(literal ".wav")
+			(literal ".wave")
+		)
+		(require-any
+			(subpath "${FRONT_USER_HOME}/tmp")
+			(subpath "/private/var/tmp")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.manageddeviced")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+								)
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+										)
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(signing-identifier "com.apple.momentsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(require-any
+						(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+						(subpath "${HOME}/Library/com.apple.momentsd")
+					)
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.momentsd")
+				)
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.momentsd")
+				(subpath "${HOME}/Library/com.apple.momentsd")
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-any
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
+	)
+)
 (deny file-read*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")

 
 (allow file-read-data
 	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.videocodecd")
 	)
 )
 (allow file-read-data
-	(require-any
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
-		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}")
-		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
+	(require-all
+		(signing-identifier "com.apple.wapic")
+		(require-any
+			(literal "/dev/bpf[0-9]")
+			(regex #"/dev/bpf([0-9])+")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist*")
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist*")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments")
+		)
+		(signing-identifier "com.apple.storagedatad")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.mDNSResponderHelper")
+		(require-any
+			(literal "/dev/bpf[0-9]")
+			(regex #"/dev/bpf([0-9])+")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/AppleInternal/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.privacyaccountingctl")
+		(literal "/dev/ttys*")
+		(regex #"^/dev/ttys([0-9])*")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/System/Developer/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-data
+	(require-all
+		(require-any
+			(subpath "/private/var/factory_mount/[^/]+/Applications")
+			(subpath "/private/var/personalized_automation/Applications")
+			(subpath "/private/var/personalized_debug/Applications")
+			(subpath "/private/var/personalized_factory/[^/]+/Applications")
+		)
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var/containers/Bundle")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/Developer/Applications")
+		(require-any
+			(signing-identifier "com.apple.managedappdistributiond")
+			(signing-identifier "com.apple.storekitd")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-read-data
+	(require-all
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
+		)
+		(signing-identifier "com.apple.chronod")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.cloudpaird")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.siriknowledged")
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.gpsd")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
+			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container-proxy")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+							(require-all
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+					(require-all
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.security.KeychainDBMover")
+		(subpath "${FRONT_USER_HOME}/Library/Keychains")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.filederivatived")
+		(extension "com.apple.spotlight-indexable")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(require-any
+			(require-all
+				(subpath "/System/Library/Carrier Bundles")
+				(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+			)
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+						(require-any
+							(require-all
+								(subpath "/System/Library/Carrier Bundles")
+								(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+							)
+							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+					(require-all
+						(subpath "/System/Library/Carrier Bundles")
+						(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.announced")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
+			(subpath "/private/var/tmp/com.apple.announced")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read-data
+	(require-all
+		(require-any
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
+		)
+		(signing-identifier "com.apple.MTLAssetUpgraderD")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.network.client")
+		(require-any
+			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
+			(literal "/private/var/db/com.apple.networkextension.tracker-info")
+			(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+			(literal "/private/var/preferences/com.apple.networkd.plist")
+			(literal "/private/var/preferences/com.apple.security.plist")
+			(require-all
+				(%entitlement-is-present "com.apple.private.networkextension.configuration")
+				(literal "/private/var/preferences/com.apple.networkextension.plist")
+			)
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(require-any
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+						(require-any
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+							(subpath "${FRONT_USER_HOME}")
+						)
+					)
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+							)
+						)
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+		(signing-identifier "com.apple.airplayd")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(signing-identifier "com.apple.siriknowledged")
+						(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+						(require-any
+							(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+							(require-all
+								(vnode-type DIRECTORY)
+								(require-any
+									(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+								)
+							)
+						)
+					)
+					(signing-identifier "com.apple.mediaartworkd")
+				)
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+						(subpath "${HOME}")
+						(require-any
+							(require-all
+								(signing-identifier "com.apple.siriknowledged")
+								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+								(require-any
+									(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+									(require-all
+										(vnode-type DIRECTORY)
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+										)
+									)
+								)
+							)
+							(signing-identifier "com.apple.mediaartworkd")
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.airplayd")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?airplayd_")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.audiomxd")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?audiomxd_")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.mediaplaybackd")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?mediaplaybackd_")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.nanophoned")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+					(require-all
+						(signing-identifier "com.apple.tursd")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
+					)
+					(require-all
+						(signing-identifier "com.apple.videocodecd")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?videocodecd_")
+							(require-all
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
+								(subpath "${HOME}")
+								(require-any
+									(require-all
+										(signing-identifier "com.apple.siriknowledged")
+										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+										(require-any
+											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+											(require-all
+												(vnode-type DIRECTORY)
+												(require-any
+													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+												)
+											)
+										)
+									)
+									(signing-identifier "com.apple.mediaartworkd")
+								)
+							)
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(signing-identifier "com.apple.siriknowledged")
+				(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+				(require-any
+					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+					(require-all
+						(vnode-type DIRECTORY)
+						(require-any
+							(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.mediaserverd.read")
+		(require-any
+			(signing-identifier "com.apple.airplayd")
+			(signing-identifier "com.apple.audiomxd")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/preferences/com.apple.security.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.mediaserverd.read-write")
+		(signing-identifier "com.apple.audiomxd")
 	)
 )
 (allow file-read-data

 )
 (allow file-read-data
 	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
-		(vnode-type REGULAR-FILE)
+		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")
+		(require-any
+			(require-any
+				(literal "/usr/standalone/firmware/apticket.der")
+				(subpath "/private/var/hardware/FactoryData")
+			)
+			(subpath "/private/preboot")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
+		(extension "com.apple.identityservices.deliver")
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+		(subpath "${FRONT_USER_HOME}")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/db/com.apple.networkextension.tracker-info")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+		(require-any
+			(require-any
+				(subpath "/private/var/factory_mount/[^/]+/Applications")
+				(subpath "/private/var/personalized_automation/Applications")
+				(subpath "/private/var/personalized_debug/Applications")
+				(subpath "/private/var/personalized_factory/[^/]+/Applications")
+			)
+			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
+			(subpath "/Applications")
+			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
+			(subpath "/private/var/containers/Bundle")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.tmpdir")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(subpath "${HOME}/Library/Fonts")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(extension "com.apple.clouddocs.version")
 	)
 )
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
+		(literal "/private/var/preferences/com.apple.security.plist")
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(require-any
+			(require-all
+				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			)
+			(require-all
+				(extension "com.apple.librarian.ubiquity-container")
+				(require-any
+					(require-all
+						(subpath "/private/var")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+						(subpath "${FRONT_USER_HOME}")
+					)
+					(subpath "${HOME}/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+				)
+			)
+			(require-all
+				(require-any
+					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
+					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+					(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
+				)
+				(require-any
+					(extension "com.apple.librarian.ubiquity-revision")
+					(require-all
+						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
+		(literal "${FRONT_USER_HOME}")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read-data
+	(require-all
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var/containers/Data/System/com.apple.geod")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
+			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(require-any
+			(require-all
+				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+				(extension "com.apple.tcc.kTCCServiceAddressBook")
+				(require-any
+					(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
+					(subpath "${HOME}/Library/AddressBook")
+					(subpath "${HOME}/Library/AddressBook/Delegates")
+				)
+			)
+			(subpath "${HOME}/Library/Fonts")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/AppleInternal")
+		(system-attribute carrier-build)
+	)
+)
 (allow file-read-data
 	(require-all
 		(extension "com.apple.assets.read")

 		)
 	)
 )
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
+		(subpath "${FRONT_USER_HOME}")
+		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/usr/local/lib")
+		(system-attribute carrier-build)
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+	)
+)
+(allow file-read-data
+	(require-all
+		(uid 0)
+		(vnode-type CHARACTER-DEVICE)
+		(%entitlement-is-bool-true "com.apple.security.ts.bpf")
+		(literal "/dev/bpf*")
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/CloudDocs/session/r")
+		(vnode-type REGULAR-FILE)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read-data
+	(require-all
+		(vnode-type DIRECTORY SYMLINK)
+		(extension "com.apple.revisiond.revision")
+		(require-any
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
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
+					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
+				)
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+					(require-all
+						(extension "com.apple.revisiond.staging")
+						(require-any
+							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/.DocumentRevisions-V100/staging")
+							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
+						)
+						(require-any
+							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
+							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
+		(process-attribute is-apple-signed-executable)
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-data
+	(require-all
+		(system-attribute developer-mode)
+		(literal "/mach.*")
+		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
+	)
+)
 (allow file-read-data
 	(require-all
 		(subpath "${HOME}/Library/Application Support/CloudDocs/session/r")

 )
 (allow file-read-data
 	(require-all
-		(literal "/private/var/db/com.apple.networkextension.tracker-info")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
+		(signing-identifier "com.apple.audiomxd")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.fileindexerd")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
+		(require-any
+			(extension "com.apple.sandbox.application-group")
+			(require-all
+				(subpath "/private/var")
+				(extension "com.apple.sandbox.container")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.geoanalyticsd")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.cameracaptured")
+		(require-any
+			(extension "com.apple.mediaserverd.read")
+			(extension "com.apple.mediaserverd.read-write")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.manageddeviced")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(require-any
+					(require-all
+						(extension "com.apple.sandbox.container")
+						(require-any
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(require-any
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+								)
+							)
+							(require-all
+								(subpath "/private/var/PersonaVolumes")
+								(require-any
+									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+									(require-all
+										(require-any
+											(subpath "${FRONT_USER_HOME}")
+											(subpath "${HOME}")
+										)
+										(require-any
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
+											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+										)
+									)
+								)
+							)
+						)
+					)
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
+					)
+				)
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.storagedatad")
+		(require-any
+			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.tursd")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(signing-identifier "com.apple.managedappdistributiond")
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+				)
+			)
+			(require-all
+				(signing-identifier "com.apple.storekitd")
+				(require-any
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+					)
+					(require-all
+						(subpath "/private/var/PersonaVolumes")
+						(require-any
+							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							(require-all
+								(require-any
+									(subpath "${FRONT_USER_HOME}")
+									(subpath "${HOME}")
+								)
+								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
+							)
+						)
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.anomalydetectiond")
+		(require-any
+			(require-all
+				(vnode-type DIRECTORY)
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+			)
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(require-any
+					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
+				)
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.nanophoned")
+		(require-any
+			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
+			)
+			(require-any
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
+				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
+			)
+			(require-any
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
+				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments(/|$)")
+						(signing-identifier "com.apple.storagedatad")
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
+						(signing-identifier "com.apple.storagedatad")
+					)
+				)
+			)
+		)
+	)
+)
+(allow file-read-data
+	(require-all
+		(signing-identifier "com.apple.mediaplaybackd")
+		(require-any
+			(extension "com.apple.mediaserverd.read")
+			(extension "com.apple.mediaserverd.read-write")
+		)
 	)
 )
 (allow file-read-data

 		)
 	)
 )
-(allow file-read-data
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-		(process-attribute is-apple-signed-executable)
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
 (allow file-read-data
 	(require-all
 		(vnode-type DIRECTORY)

 		)
 	)
 )
-(allow file-read-data
-	(require-all
-		(system-attribute developer-mode)
-		(literal "/mach.*")
-		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
-	)
-)
 (allow file-read-data
 	(require-all
 		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-		(subpath "${FRONT_USER_HOME}")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 		(require-any
 			(require-all
-				(subpath "/System/Library/Carrier Bundles")
-				(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-			)
-			(require-all
-				(subpath "/private/var")
+				(subpath "${FRONT_USER_HOME}")
 				(require-any
 					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-						(require-any
-							(require-all
-								(subpath "/System/Library/Carrier Bundles")
-								(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-							)
-							(subpath "${FRONT_USER_HOME}")
-						)
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
 					)
 					(require-all
-						(subpath "/System/Library/Carrier Bundles")
-						(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+				)
+			)
+			(require-all
+				(subpath "${HOME}")
+				(require-any
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
+					)
+					(require-all
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
+						(signing-identifier "com.apple.MTLAssetUpgraderD")
 					)
 				)
 			)
 		)
 	)
 )
-(allow file-read-data
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
-				(extension "com.apple.tcc.kTCCServiceAddressBook")
-				(require-any
-					(literal "${HOME}/Library/Preferences/com.apple.mobilephone.speeddial.plist")
-					(subpath "${HOME}/Library/AddressBook")
-					(subpath "${HOME}/Library/AddressBook/Delegates")
-				)
-			)
-			(subpath "${HOME}/Library/Fonts")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
-		(subpath "${FRONT_USER_HOME}")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
 (allow file-read-data
 	(require-all
 		(vnode-type REGULAR-FILE)

 		)
 	)
 )
-(allow file-read-data
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.tmpdir")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-			(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.tmpdir}")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.cloudpaird")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.cloudpaird")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r")
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")
-		(require-any
-			(require-any
-				(literal "/usr/standalone/firmware/apticket.der")
-				(subpath "/private/var/hardware/FactoryData")
-			)
-			(subpath "/private/preboot")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "${FRONT_USER_HOME}/Library/Caches/GeoServices")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.mediaserverd.read")
-		(require-any
-			(signing-identifier "com.apple.airplayd")
-			(signing-identifier "com.apple.audiomxd")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/AppleInternal")
-		(system-attribute carrier-build)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.linkd")
-		(require-any
-			(require-any
-				(subpath "/private/var/factory_mount/[^/]+/Applications")
-				(subpath "/private/var/personalized_automation/Applications")
-				(subpath "/private/var/personalized_debug/Applications")
-				(subpath "/private/var/personalized_factory/[^/]+/Applications")
-			)
-			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-			(subpath "/AppleInternal/Applications")
-			(subpath "/Applications")
-			(subpath "/Developer/Applications")
-			(subpath "/System/Developer/Applications")
-			(subpath "/private/var/containers/Bundle")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.mediaserverd.read-write")
-		(signing-identifier "com.apple.audiomxd")
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.airplayd")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.network.client")
-		(require-any
-			(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-			(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.nsurlstoragedresources/Library/dafsaData.bin")
-			(literal "/private/var/db/com.apple.networkextension.tracker-info")
-			(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
-			(literal "/private/var/preferences/com.apple.networkd.plist")
-			(literal "/private/var/preferences/com.apple.security.plist")
-			(require-all
-				(%entitlement-is-present "com.apple.private.networkextension.configuration")
-				(literal "/private/var/preferences/com.apple.networkextension.plist")
-			)
-			(require-all
-				(process-attribute is-apple-signed-executable)
-				(require-any
-					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.fileindexerd")
-		(require-any
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$)")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-						(require-any
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-							(subpath "${FRONT_USER_HOME}")
-						)
-					)
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+(/|$)")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+(/|$)")
-					)
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.cameracaptured")
-		(require-any
-			(extension "com.apple.mediaserverd.read")
-			(extension "com.apple.mediaserverd.read-write")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.geoanalyticsd")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.geoanalyticsd")
-				)
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.geoanalyticsd")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(regex #"(((^/private/var/((mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData($|/com\.apple\.chrono(/|$))|[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData$)|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.chrono(/|$))")
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.siriknowledged")
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Podcasts.+\.plist$")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.chrono")
-		)
-		(signing-identifier "com.apple.chronod")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.CoreDevice.dtfilesandboxd")
-		(require-any
-			(extension "com.apple.sandbox.application-group")
-			(require-all
-				(subpath "/private/var")
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
 (allow file-read-data
 	(require-all
 		(signing-identifier "com.apple.momentsd")

 )
 (allow file-read-data
 	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read-data
-	(require-all
-		(require-any
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com.apple[^/]+/com.apple.metal")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches/com[^/]+/com.apple.metal")
-		)
-		(signing-identifier "com.apple.MTLAssetUpgraderD")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Caches/com.apple.metalassetupgrader(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Caches/[^/]+/com.apple.metal(/|$)")
-						(signing-identifier "com.apple.MTLAssetUpgraderD")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.manageddeviced")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-								)
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/[^/]+\.plist$")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-										)
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/StoreKit(/|$)")
-					)
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/StoreKit")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.announced")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.announced")
-			(subpath "/private/var/tmp/com.apple.announced")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.anomalydetectiond")
-		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-			)
-			(require-all
-				(vnode-type REGULAR-FILE)
-				(require-any
-					(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.anomalydetectiond")
-				)
-			)
-			(subpath "${HOME}/Library/Caches/com.apple.anomalydetectiond")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.security.KeychainDBMover")
-		(subpath "${FRONT_USER_HOME}/Library/Keychains")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.gpsd")
-		(require-any
-			(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/gpsd")
-			(subpath "${FRONT_USER_HOME}/Library/Logs/gpsd")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.mediaplaybackd")
-		(require-any
-			(extension "com.apple.mediaserverd.read")
-			(extension "com.apple.mediaserverd.read-write")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/SystemData/com.apple.mediaserverd")
-		(signing-identifier "com.apple.mediaplaybackd")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			)
-			(require-all
-				(extension "com.apple.librarian.ubiquity-container")
-				(require-any
-					(require-all
-						(subpath "/private/var")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-						(subpath "${FRONT_USER_HOME}")
-					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				)
-			)
-			(require-all
-				(require-any
-					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore")
-					(subpath "${HOME}/Library/Application Support/Ubiquity/genstore/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-					(subpath "${HOME}/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/Ubiquity/genstore")
-				)
-				(require-any
-					(extension "com.apple.librarian.ubiquity-revision")
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.nanophoned")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-			)
-			(require-any
-				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments(/|$)")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist")
-						(signing-identifier "com.apple.storagedatad")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container-proxy")
-		(require-any
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-							(require-all
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-								(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-					(require-all
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-						(signing-identifier "com.apple.CoreDevice.dtfileserviced")
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.mDNSResponderHelper")
-		(require-any
-			(literal "/dev/bpf[0-9]")
-			(regex #"/dev/bpf([0-9])+")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.videocodecd")
-	)
-)
-(allow file-read-data
-	(require-all
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Preferences/com.apple.mobilesafari.plist*")
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/WebExtensions/Extensions.plist*")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/TapToRadar/Attachments")
-		)
-		(signing-identifier "com.apple.storagedatad")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.privacyaccountingctl")
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.wapic")
-		(require-any
-			(literal "/dev/bpf[0-9]")
-			(regex #"/dev/bpf([0-9])+")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(signing-identifier "com.apple.managedappdistributiond")
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-				)
-			)
-			(require-all
-				(signing-identifier "com.apple.storekitd")
-				(require-any
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(require-any
-							(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+(/Library/Caches)?/StoreKit(/|$)")
-							)
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.tursd")
-		(require-any
-			(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync")
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-wal")
-			)
-			(require-any
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-journal")
-				(literal "${FRONT_USER_HOME}/Library/Logs/CompanionSync/statistics.db-shm")
-			)
-			(require-any
-				(subpath "${FRONT_USER_HOME}/Library/Logs/CompanionSync/TransportLogs")
-				(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/DiagnosticLogs/CompanionSync/TransportLogs")
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "${FRONT_USER_HOME}/Containers/Bundle")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.storagedatad")
-		(require-any
-			(literal "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist*")
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Safari/Downloads/Downloads.plist")
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(require-any
-			(subpath "/private/var/factory_mount/[^/]+/Applications")
-			(subpath "/private/var/personalized_automation/Applications")
-			(subpath "/private/var/personalized_debug/Applications")
-			(subpath "/private/var/personalized_factory/[^/]+/Applications")
-		)
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/Applications")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/AppleInternal/Applications")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-data
-	(require-all
-		(signing-identifier "com.apple.audiomxd")
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
-		(subpath "${FRONT_USER_HOME}/Library/IdentityServices")
-		(extension "com.apple.identityservices.deliver")
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "/private/var/preferences/com.apple.security.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
-		(literal "/private/var/preferences/com.apple.security.plist")
-	)
-)
-(allow file-read-data
-	(require-all
-		(vnode-type DIRECTORY SYMLINK)
-		(extension "com.apple.revisiond.revision")
-		(require-any
-			(require-all
-				(extension "com.apple.revisiond.staging")
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/.DocumentRevisions-V100/staging")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-				)
-				(require-any
-					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-				)
-			)
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID")
-					(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/PerUID/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "${FRONT_USER_HOME}/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/.DocumentRevisions-V100/PerUID")
-					(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/PerUID")
-				)
-				(require-any
-					(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-					(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-					(require-all
-						(extension "com.apple.revisiond.staging")
-						(require-any
-							(subpath "${FRONT_USER_HOME}/.DocumentRevisions-V100/staging")
-							(subpath "/private/var/.DocumentRevisions-V100/staging")
-							(subpath "/private/var/PersonaVolumes/[^/]+/.DocumentRevisions-V100/staging")
-						)
-						(require-any
-							(%entitlement-is-bool-true "com.apple.security.ts.revisiond-client")
-							(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-						)
-					)
-				)
-			)
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(uid 0)
-		(vnode-type CHARACTER-DEVICE)
-		(%entitlement-is-bool-true "com.apple.security.ts.bpf")
-		(literal "/dev/bpf*")
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.read-any-bundle")
+		(signing-identifier "com.apple.linkd")
 		(require-any
 			(require-any
 				(subpath "/private/var/factory_mount/[^/]+/Applications")

 	)
 )
 (allow file-read-data
-	(require-all
-		(subpath "/private/var/containers/Data/System/com.apple.geod")
-		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.security.daemon-container")
-			(%entitlement-is-bool-true "com.apple.security.ts.daemon-container")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
-		(literal "${FRONT_USER_HOME}")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/System/Developer/Applications")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var/containers/Bundle")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(subpath "${HOME}/Library/Fonts")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/Developer/Applications")
-		(require-any
-			(signing-identifier "com.apple.managedappdistributiond")
-			(signing-identifier "com.apple.storekitd")
-		)
-	)
-)
-(allow file-read-data
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
-	)
-)
-(allow file-read-data
-	(require-all
-		(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-data
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(require-all
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-				(subpath "${HOME}")
-				(require-any
-					(require-all
-						(signing-identifier "com.apple.siriknowledged")
-						(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-						(require-any
-							(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-							(require-all
-								(vnode-type DIRECTORY)
-								(require-any
-									(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-								)
-							)
-						)
-					)
-					(signing-identifier "com.apple.mediaartworkd")
-				)
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(require-all
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-						(subpath "${HOME}")
-						(require-any
-							(require-all
-								(signing-identifier "com.apple.siriknowledged")
-								(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-								(require-any
-									(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-									(require-all
-										(vnode-type DIRECTORY)
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-										)
-									)
-								)
-							)
-							(signing-identifier "com.apple.mediaartworkd")
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.airplayd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?airplayd_")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.audiomxd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?audiomxd_")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.mediaplaybackd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?mediaplaybackd_")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.nanophoned")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-					(require-all
-						(signing-identifier "com.apple.tursd")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync/(nms\.)?com\.apple\.private\.alloy\.voicemailsync")
-					)
-					(require-all
-						(signing-identifier "com.apple.videocodecd")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Logs/CrashReporter/(Retired/)?(\.)?videocodecd_")
-							(require-all
-								(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes/Artwork(/|$)")
-								(subpath "${HOME}")
-								(require-any
-									(require-all
-										(signing-identifier "com.apple.siriknowledged")
-										(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-										(require-any
-											(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-											(require-all
-												(vnode-type DIRECTORY)
-												(require-any
-													(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-													(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-												)
-											)
-										)
-									)
-									(signing-identifier "com.apple.mediaartworkd")
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${HOME}")
-				(signing-identifier "com.apple.siriknowledged")
-				(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-				(require-any
-					(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-					(require-all
-						(vnode-type DIRECTORY)
-						(require-any
-							(regex #"(((^/private/var/((((mobile|euser[0-9]+)/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(((-journal|-shm)|-wal))?|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|[-0-9A-F]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb(-journal|-shm))|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb-wal)|^/private/var/Users/[^/]+/Media/([^/]+/)?iTunes_Control/iTunes/MediaLibrary.sqlitedb)")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control/iTunes$")
-						)
-					)
-				)
-			)
-		)
+	(require-any
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-only}")
+		(literal "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/NanoPreferencesSync/NanoDomains/${ENTITLEMENT:com.apple.security.ts.nano-preference.read-write}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-only}")
+		(subpath "${FRONT_USER_HOME}/Library/DeviceRegistry/${ANY_UUID}/${ENTITLEMENT:com.apple.security.ts.nano-paired-storage.subpath.read-write}")
 	)
 )
 (deny file-read-data

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
-		(subpath "${FRONT_USER_HOME}")
-		(signing-identifier "com.apple.nanophoned")
+		(signing-identifier "com.apple.security.KeychainDBMover")
+		(subpath "${FRONT_USER_HOME}/Library/Keychains")
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(subpath "${HOME}/Library/Fonts")
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/CompanionSync$")
+		(subpath "${FRONT_USER_HOME}")
+		(signing-identifier "com.apple.nanophoned")
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(signing-identifier "com.apple.security.KeychainDBMover")
-		(subpath "${FRONT_USER_HOME}/Library/Keychains")
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(subpath "${HOME}/Library/Fonts")
 	)
 )
 (allow file-read-metadata

 		(literal "/dev/bpf*")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(signing-identifier "com.apple.filederivatived")
+		(extension "com.apple.spotlight-indexable")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(extension "com.apple.mediaserverd.read-write")

 		(literal "${HOME}/Library/PPTDevice")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(subpath "/Applications")
-		(signing-identifier "com.apple.managedappdistributiond")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "/AppleInternal")

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/System/Developer/Applications")
+		(subpath "/Applications")
 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(require-any
-			(subpath "/private/var/factory_mount/[^/]+/Applications")
-			(subpath "/private/var/personalized_automation/Applications")
-			(subpath "/private/var/personalized_debug/Applications")
-			(subpath "/private/var/personalized_factory/[^/]+/Applications")
-		)
+		(subpath "/System/Developer/Applications")
 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/AppleInternal/Applications")
+		(require-any
+			(subpath "/private/var/factory_mount/[^/]+/Applications")
+			(subpath "/private/var/personalized_automation/Applications")
+			(subpath "/private/var/personalized_debug/Applications")
+			(subpath "/private/var/personalized_factory/[^/]+/Applications")
+		)
 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )

 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(subpath "/AppleInternal/Applications")
+		(signing-identifier "com.apple.managedappdistributiond")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(extension "com.apple.sandbox.container")

 )
 (allow file-read-xattr
 	(require-all
-		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
-		(signing-identifier "com.apple.mediaplaybackd")
+		(signing-identifier "com.apple.filederivatived")
+		(extension "com.apple.spotlight-indexable")
 	)
 )
 (allow file-read-xattr

 )
 (allow file-read-xattr
 	(require-all
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+		(literal "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(signing-identifier "com.apple.mediaplaybackd")
 	)
 )

 		)
 	)
 )
+(allow file-read-xattr
+	(require-all
+		(require-any
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
+		)
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.mediaserverd(/|$)")
+		(signing-identifier "com.apple.mediaplaybackd")
+	)
+)
 (allow file-read-xattr
 	(require-all
 		(literal "${FRONT_USER_HOME}/Library/Preferences/com.apple.carrier.plist")

 )
 (allow file-read-xattr
 	(require-all
-		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+		(subpath "${FRONT_USER_HOME}")
+		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(subpath "${HOME}/Library/Fonts")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
+		(literal "/private/var/preferences/com.apple.security.plist")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")
+		(require-any
+			(require-any
+				(literal "/usr/standalone/firmware/apticket.der")
+				(subpath "/private/var/hardware/FactoryData")
+			)
+			(subpath "/private/preboot")
+		)
 	)
 )
 (allow file-read-xattr

 		(extension "com.apple.clouddocs.version")
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
-		(require-any
-			(subpath "${FRONT_USER_HOME}")
-			(subpath "${HOME}")
-		)
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(extension "com.apple.clouddocs.version")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
-		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
-	)
-)
 (allow file-read-xattr
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.front-user-home-literal.read-only")
 		(literal "${FRONT_USER_HOME}")
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
-		(literal "/private/var/preferences/com.apple.security.plist")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "/private/var/db/com.apple.networkextension.tracker-info")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(literal "/private/var/preferences/com.apple.security.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
 (allow file-read-xattr
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")

 		)
 	)
 )
-(allow file-read-xattr
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkd.plist")
-		(%entitlement-is-bool-true "com.apple.security.network.server")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-		(subpath "${HOME}/Library/Fonts")
-	)
-)
-(allow file-read-xattr
-	(require-all
-		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
-		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
-	)
-)
 (allow file-read-xattr
 	(require-all
 		(%entitlement-is-present "com.apple.security.ts.tmpdir")

 )
 (allow file-read-xattr
 	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.read-factory-files")
+		(subpath "/private/var")
+		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/iCloudDrive/[^/]+/session/r(/|$)")
 		(require-any
-			(require-any
-				(literal "/usr/standalone/firmware/apticket.der")
-				(subpath "/private/var/hardware/FactoryData")
-			)
-			(subpath "/private/preboot")
+			(subpath "${FRONT_USER_HOME}")
+			(subpath "${HOME}")
 		)
+		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
+		(extension "com.apple.clouddocs.version")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkd.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "/private/var/preferences/com.apple.security.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(literal "/private/var/preferences/com.apple.NetworkStatistics.plist")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
+	)
+)
+(allow file-read-xattr
+	(require-all
+		(%entitlement-is-present "com.apple.security.ts.system-tmpdir")
+		(subpath "/private/var/tmp/${ENTITLEMENT:com.apple.security.ts.system-tmpdir}")
 	)
 )
 (allow file-read-xattr

 )
 (allow file-read-xattr
 	(require-all
-		(subpath "/System/Library/Carrier Bundles")
-		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
+		(literal "/private/var/db/com.apple.networkextension.tracker-info")
+		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
 (allow file-read-xattr
 	(require-all
-		(subpath "/private/var")
-		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-		(subpath "${FRONT_USER_HOME}")
+		(subpath "/System/Library/Carrier Bundles")
+		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
 		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )

 	)
 )
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-issue-extension
+(allow iokit-get-properties
 	(require-all
 		(extension-class "com.apple.webkit.extension.iokit")
 		(%entitlement-is-present "com.apple.security.ts.webkit-client")
 	)
 )
-(allow iokit-issue-extension
+(allow iokit-get-properties
 	(require-all
 		(extension-class "com.apple.spotlight.extension.iosurface")
 		(signing-identifier "com.apple.filederivatived")
 	)
 )
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "ANEClientHintsUserClient")
 		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")
 		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(extension "com.apple.security.exception.iokit-user-client-class")
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(require-any
 			(iokit-registry-entry-class "AppleVirtIONeuralEngineDeviceUserClient")

 		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "IOMobileFramebufferUserClient")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "RootDomainUserClient")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(system-attribute virtual-device)
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")

 	)
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(%entitlement-is-present "com.apple.security.exception.iokit-user-client-class")
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "AppleKeyStore")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "AGXAcceleratorG*")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "IOPMrootDomain")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "AppleKeyStore")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(require-any
 			(iokit-registry-entry-class "AppleCLCD*")

 	)
 )
 
-(allow iokit-set-properties
+(allow iokit-open-service
 	(signing-identifier "com.apple.SoundBoard")
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-property "BondManagement")
 		(iokit-registry-entry-class "AppleEmbeddedBluetoothDeviceManagement")
 		(signing-identifier "com.apple.BTLEServer")
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-property "exclusive access owner")
 		(iokit-registry-entry-class "IOAudio2Device")

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(signing-identifier "com.apple.thermalmonitord")
 		(require-any

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-property "kAppleI2CEthernetLomEnable")
 		(iokit-registry-entry-class "AppleI2CEthernetAquantiaControllerBSD")
 		(signing-identifier "com.apple.lightsoutmanagementd")
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "IOHIDLibUserClient")
 		(signing-identifier "com.apple.GameController.gamecontrollerd")

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-property "Enable")
 		(iokit-registry-entry-class "AppleHDMIPortControl")
 		(signing-identifier "com.apple.audiomxd")
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-property "voice-trigger-configuration")
 		(iokit-registry-entry-class "com_apple_audio_IOBorealisOwlUserClient")
 		(signing-identifier "com.apple.audiomxd")
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "IOPMrootDomain")
 		(signing-identifier "com.apple.SurfBoard")

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-property "System Latency")
 		(require-any

 		(signing-identifier "com.apple.audiomxd")
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "ANEClientHintsUserClient")
 		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")

 		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-property "kPropertyConfiguration")
 		(iokit-registry-entry-class "AppleAOPVoiceTriggerUserClient")

 	)
 )
 
-(allow ipc-posix-sem*
+(allow ipc-posix*
 	(require-all
 		(ipc-posix-name "installcood.f.*")
 		(signing-identifier "com.apple.managedappdistributiond")
 	)
 )
-(allow ipc-posix-sem*
+(allow ipc-posix*
 	(require-all
 		(ipc-posix-name "purplebuddy.sentinel")
 		(require-any

 		)
 	)
 )
-(allow ipc-posix-sem*
+(allow ipc-posix*
 	(require-any
 		(extension "com.apple.sandbox.application-group")
 		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-sem}")
 	)
 )
 
-(allow ipc-posix-shm*
+(allow ipc-posix-sem-wait
 	(require-all
 		(ipc-posix-name "/FBW[0-9]:com.apple.frontboard.syst")
 		(signing-identifier "com.apple.SurfBoard")
 	)
 )
-(allow ipc-posix-shm*
+(allow ipc-posix-sem-wait
 	(require-all
 		(ipc-posix-name "com.apple.bgst.backup*")
 		(signing-identifier "com.apple.dasd")
 	)
 )
-(allow ipc-posix-shm*
+(allow ipc-posix-sem-wait
 	(require-all
 		(ipc-posix-name "AppleABL.*")
 		(signing-identifier "com.apple.audiomxd")
 	)
 )
-(allow ipc-posix-shm*
+(allow ipc-posix-sem-wait
 	(require-any
 		(extension "com.apple.sandbox.application-group")
 		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm}")
 	)
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "/FBW[0-9]:com.apple.frontboard.syst*")
 		(require-any

 		)
 	)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "/com.apple.AppSSO.version")
 		(require-any

 		)
 	)
 )
+(allow ipc-posix-shm*
+	(require-all
+		(ipc-posix-name "/FBW[0-9]:com.apple.frontboard.syst")
+		(signing-identifier "com.apple.SurfBoard")
+	)
+)
+(allow ipc-posix-shm*
+	(require-all
+		(ipc-posix-name "com.apple.bgst.backup*")
+		(signing-identifier "com.apple.dasd")
+	)
+)
+(allow ipc-posix-shm*
+	(require-all
+		(ipc-posix-name "apple.shm.notification_center")
+		(%entitlement-is-bool-true "com.apple.security.on-demand-install-capable")
+	)
+)
+(allow ipc-posix-shm*
+	(require-all
+		(ipc-posix-name "AppleABL.*")
+		(signing-identifier "com.apple.audiomxd")
+	)
+)
+(allow ipc-posix-shm*
+	(require-any
+		(extension "com.apple.sandbox.application-group")
+		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm.read-only}")
+		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm}")
+	)
+)
+
 (allow ipc-posix-shm-read-data
 	(require-all
 		(ipc-posix-name "/FBW[0-9]:com.apple.frontboard.syst")

 )
 (allow ipc-posix-shm-read-data
 	(require-all
-		(ipc-posix-name "apple.shm.notification_center")
-		(%entitlement-is-bool-true "com.apple.security.on-demand-install-capable")
+		(ipc-posix-name "/FBW[0-9]:com.apple.frontboard.syst*")
+		(require-any
+			(require-any
+				(signing-identifier "com.apple.ClarityBoard")
+				(signing-identifier "com.apple.SoundBoard")
+			)
+			(signing-identifier "com.apple.Carousel")
+		)
 	)
 )
 (allow ipc-posix-shm-read-data

 (allow ipc-posix-shm-read-data
 	(require-any
 		(extension "com.apple.sandbox.application-group")
-		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm.read-only}")
 		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm}")
 	)
 )

 	)
 )
 
-(deny isp-command-send
+(deny ipc-sysv-shm
 	(require-all
 		(signing-identifier "com.apple.cameracaptured")
 		(isp-command

 			CISP_CMD_FLICKER_SENSOR_SET
 			CISP_CMD_CED_DISABLE
 			CISP_CMD_ALS_SENSOR_POWER_SET
-			CISP_CMD_CH_START
 			CISP_CMD_CH_STOP
-			CISP_CMD_CH_RAW_FRAME_PROCESS
-			CISP_CMD_CH_SET_FILE_LOAD
-			CISP_CMD_CH_RAW_FRAME_PROCESS_GO
-			CISP_CMD_CH_DATA_FILE_LOAD
-			CISP_CMD_CH_CAMERA_ALIGNMENT_CAL_SET
-			CISP_CMD_CH_GENERAL_PROCESS
-			CISP_CMD_CH_OIS_EXTENDED_STROKE_SET
-			CISP_CMD_CH_GENERAL_PROCESS_GENERIC_REQUEST
-			CISP_CMD_CH_CAMERA_APS_RECAL_SET
-			CISP_CMD_CH_LSC_POLYNOMIAL_COEFF_GET
-			CISP_CMD_CH_SYSCFG_KEY_SET
-			CISP_CMD_CH_DATA_FILE_MULTIPLE_LOAD
-			CISP_CMD_CH_HW_INFO_GET
-			CISP_CMD_CH_CAMERA_AGILE_FREQ_ARRAY_CURRENT_GET
-			CISP_CMD_CH_DATA_FILE_UNLOAD
-			CISP_CMD_CH_GENERAL_PROCESS_BUFFERS
-			CISP_CMD_CH_LPDP_HS_RECEIVER_TUNING_SET
-			CISP_CMD_CH_SENSOR_PERMODULE_LSC_QUADRA_CH_SHADING_GET
+			CISP_CMD_CH_RESET
+			CISP_CMD_CH_RAW_FRAME_PROCESS_START
+			CISP_CMD_CH_CAPTURE_MODE_SET
+			CISP_CMD_CH_EDGE_MAP_CONFIG_GET
+			CISP_CMD_CH_CAMERA_MIPI_FREQ_CURRENT_GET
+			CISP_CMD_CH_TIMEMACHINE_DEPTH_SET
+			CISP_CMD_CH_DSC_STREAMING_MODE_SET
+			CISP_CMD_CH_MS_SYNC_SET
+			CISP_CMD_CH_MS_SELECT_MASTER
+			CISP_CMD_CH_SLAVE_CAMERA_PROCESSING_CONFIG
+			CISP_CMD_CH_CAMERA_CHARGEPUMP_FREQUENCY_TOTAL_GET
+			CISP_CMD_CH_CAMERA_PROCESSING_CONFIG
+			CISP_CMD_CH_MIN_FRAME_SKIPPING_RATIO
+			CISP_CMD_CH_BUFFER_POOL_RETURN
+			CISP_CMD_CH_CAMERA_AGILE_FREQ_ARRAY_TOTAL_GET
+			CISP_CMD_CH_PRIMARY_FRAME_SKIPPING_RATIO
+			CISP_CMD_CH_EXTERNAL_SYNC_CONFIG
+			CISP_CMD_CH_SENSOR_PUBLIC_KEY
 			CISP_CMD_CH_SENSOR_SECURE_INFO
 			CISP_CMD_CH_SENSOR_STATUS_GET
 			CISP_CMD_CH_SENSOR_BOOT
-			CISP_CMD_CH_SENSOR_PERMODULE_LUMA_SHADING_GET
-			CISP_CMD_CH_SENSOR_PDP_GET
-			CISP_CMD_CH_SENSOR_PERMODULE_GIC_GET
-			CISP_CMD_CH_SENSOR_PERMODULE_DSC_GET
+			CISP_CMD_CH_SENSOR_FOCUS_PIXEL_MAPS_GET
+			CISP_CMD_CH_SENSOR_HOST_AUTHORIZATION_SET
+			CISP_CMD_CH_SENSOR_STATIC_RAWPROC_DPC_GET
+			CISP_CMD_CH_SENSOR_SERIAL_NUMBER_GET
 			CISP_CMD_CH_SENSOR_PERMODULE_XHATCH_GET
-			CISP_CMD_CH_PROJECTOR_USAGE_GET
-			CISP_CMD_CH_STATUS_LED_THR_GET
-			CISP_CMD_CH_FACE_DETECTION_OFFLINE
-			CISP_CMD_CH_FACE_DETECTION_CAMERA_EXTRINSICS
-			CISP_CMD_CH_FRAMEDONE_TIMEOUT
-			CISP_CMD_CH_FOCUS_DRIVER_INIT_FAILED
+			CISP_CMD_CH_SENSOR_HASHCODE_SET
+			CISP_CMD_CH_PROX_OFF
+			CISP_CMD_CH_LC_DYNAMIC_VOLTAGE_ENABLE
+			CISP_CMD_CH_FACE_DETECTION_OFFLINE_STOP
+			CISP_CMD_CH_AICAM_DISABLE
 			CISP_CMD_CH_ERROR_NOTIFICATION
 			CISP_CMD_CH_POWER_CONTROL
 			CISP_CMD_CH_SIGNPOST_NOTIFICATION

 			CISP_CMD_MCACHE_REQUEST
 			CISP_CMD_MCACHE_UPDATE
 			CISP_CMD_MCACHE_RELEASE
-			CISP_CMD_CIL_BREAKER_ACTIVATED
-			CISP_CMD_CH_REGISTER_COUNTERS_NOTIFICATION
+			CISP_CMD_CH_ISP_LINE_INTERRUPT
+			CISP_CMD_BORA_STATUS
 			CISP_CMD_CH_TAILSPIN_NOTIFICATION
-			CISP_CMD_CH_CURRENT_DISPLAY_BRIGHTNESS_UPDATE
-			CISP_CMD_CH_FID_ENABLE
-			CISP_CMD_CH_ATTN_ENABLE
+			CISP_CMD_CH_NVSTORAGE_INFO_GET
+			CISP_CMD_CH_NVSTORAGE_DATA_GET
+			CISP_CMD_CH_HI_RES_HITH_THUMBNAIL_MAX_SIZE_GET
 			CISP_CMD_CH_ATTN_ONLINE_CUSTOM
-			CISP_CMD_IPC_ENDPOINT_SET2
-			CISP_CMD_IPC_ENDPOINT_UNSET2
-			CISP_CMD_SET_DSID_CLR_MULTI_BC_REG_BASE
-			CISP_CMD_MULTICAM_SESSION_CREATE
-			CISP_CMD_MULTICAM_SESSION_DESTROY
-			CISP_CMD_CH_MC_AOP_ISP_INFO_SET
-			CISP_CMD_CH_MC_AOP_ISP_ENDPOINT_INFO_SET2
-			CISP_CMD_AON_PTD_SET
-			CISP_CMD_BACK_CHANNEL_RPC)
+			CISP_CMD_IPC_ENDPOINT_SET
+			CISP_CMD_IPC_ENDPOINT_UNSET
+			CISP_CMD_CH_VIO_SET_CONFIG
+			CISP_CMD_CH_VIO_SET_BLOB_SIZE
+			CISP_CMD_CH_TOF_FRAME_SET
+			CISP_CMD_MULTICAM_ZOOM
+			CISP_CMD_MULTICAM_SESSION_STATUS
+			CISP_CMD_CH_MC_DATARATE_SET
+			CISP_CMD_CH_VIS_CONTROL
+			CISP_CMD_CH_VIS_ALG_PARAMETER
+			CISP_CMD_CH_DISTORTION_DATA_GET)
 	)
 )
 
-(allow job-creation
+(allow isp-command-send
 	(signing-identifier "com.apple.security.cryptexd")
 )
-(deny job-creation)
+(deny isp-command-send)
 
-(deny lsopen
+(deny job-creation
 	(profile-flag "deny-lsopen")
 )
 
-(allow mach-bootstrap)
+(allow mach*)
 
-(allow mach-cross-domain-lookup)
-
-(allow mach-derive-port)
-
-(allow mach-issue-extension
+(allow mach-host-special-port-set
 	(require-all
 		(extension-class "com.apple.spotlight.extension.service")
 		(require-any

 		)
 	)
 )
-(allow mach-issue-extension
+(allow mach-host-special-port-set
 	(require-all
 		(signing-identifier "com.apple.deviceaccessd")
 		(require-any

 		)
 	)
 )
-(allow mach-issue-extension
+(allow mach-host-special-port-set
 	(require-all
 		(extension-class "com.apple.webkit.extension.mach")
 		(%entitlement-is-present "com.apple.security.ts.webkit-client")
 	)
 )
-(allow mach-issue-extension
+(allow mach-host-special-port-set
 	(require-all
 		(signing-identifier "com.apple.audiomxd")
 		(require-any

 	)
 )
 
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.chrono.event-service.*")
 		(signing-identifier "com.apple.chronod")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.awdd")
 		(signing-identifier "com.apple.tursd")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.powerlog.plxpclogger.xpc")
 		(signing-identifier "com.apple.FTLivePhotoService")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.marco")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.locationd.spi")
 		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.marco")
 		(signing-identifier "com.apple.Carousel")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.itunescloudd.xpc")
 		(signing-identifier "com.apple.siriknowledged")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "*")
 		(signing-identifier "com.apple.chronod")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.identityservicesd.embedded.auth")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.identityservicesd.embedded.auth")
 		(signing-identifier "com.apple.facetimemessagestored")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.marco")
 		(signing-identifier "com.apple.facetimemessagestored")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.marco")
 		(signing-identifier "com.apple.asktod")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.identityservicesd.embedded.auth")
 		(signing-identifier "com.apple.asktod")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.network.client")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.private.appintents.delegate.*")
 		(signing-identifier "com.apple.linkd")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.iokit.powerdxpc")
 		(signing-identifier "com.apple.FTLivePhotoService")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.AGXCompilerService*")
 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.ImageIOXPCService")
 		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-any
 			(global-name "com.apple.cvmsServ")

 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.quicklook.ThumbnailsAgent")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.MTLCompilerService")
 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.mobile.heartbeat")
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.networkscored")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name ".viewservice")
 		(%entitlement-is-bool-true "com.apple.security.ts.viewservice.client")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.nesessionmanager")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.securityd")
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.trustd")
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.AppSSO.service-xpc")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.dnssd.service")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.medialibraryd.xpc")
 		(signing-identifier "com.apple.siriknowledged")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.marco")
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.cloudd")
 		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.ImageIOXPCService")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-any
 			(global-name "com.apple.ckdiscretionaryd")

 		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.locationd.synchronous")
 		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.spotlight.IndexAgent")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.spotlight.IndexDelegateAgent")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(process-attribute is-apple-signed-executable)
 		(global-name "com.apple.audioanalyticsd")
 		(%entitlement-is-bool-true "com.apple.security.ts.play-audio")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.identityservicesd.idquery.embedded.auth")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.appleneuralengine")
 		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.accountsd.accountmanager")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.cmfsyncagent.embedded.auth")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.ABDatabaseDoctor")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.contactsd")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.powerlog.plxpclogger.xpc")
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-any
 			(global-name "com.apple.geod")

 		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.locationd.registration")
 		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.geoanalyticsd")
 		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.iokit.powerdxpc")
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.DiagnosticExtensions.*")
 		(signing-identifier "com.apple.diagnosticextensionsd")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.*")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.power-assertions")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-present "com.apple.security.ts.webkit-client")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.FileCoordination")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.springboard-services")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.revisiond")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(signing-identifier "com.apple.internal.livtipsd")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(signing-identifier "com.apple.asktod")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "*")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.play-audio")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(signing-identifier "com.apple.Carousel")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.identityservicesd.embedded.auth")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(signing-identifier "com.apple.facetimemessagestored")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.remotemanagement.*")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.PowerManagement.control")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.usernotifications.delegate.*")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.PowerManagement.control")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.identityservicesd.embedded.auth")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(signing-identifier "com.apple.usernotificationsd")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.system.notification_center")
 		(%entitlement-is-bool-true "com.apple.security.on-demand-install-capable")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(extension "com.apple.sandbox.application-group")
 		(extension "com.apple.security.exception.mach-lookup.global-name")

 		(global-name "com.apple.tccd")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-any
 		(xpc-service-name "com.apple.CoreGraphics.CGPDFService")
 		(xpc-service-name "com.apple.WebKit.*")
 	)
 )
 
-(allow mach-priv-task-port
+(allow mach-priv-host-port
 	(require-all
 		(system-attribute developer-mode)
 		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
 	)
 )
 
-(allow mach-register
+(allow mach-priv-task-port
 	(require-any
 		(extension "com.apple.sandbox.application-group")
 		(extension "com.apple.security.exception.mach-register.global-name")
 	)
 )
 
-(allow mach-task-exception-port-set)
-
-(allow mach-task-inspect
+(allow mach-task-exception-port-set
 	(require-all
 		(system-attribute developer-mode)
 		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
 	)
 )
-(allow mach-task-inspect
+(allow mach-task-exception-port-set
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.ts.mach-task-read")
 		(signing-identifier "com.apple.gputoolsserviced")

 	)
 )
 
-(allow mach-task-name
+(allow mach-task-inspect
 	(require-all
 		(system-attribute developer-mode)
 		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
 	)
 )
-(allow mach-task-name
+(allow mach-task-inspect
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.ts.mach-task-name")
 		(%entitlement-is-bool-true "com.apple.security.ts.mach-task-read")

 	)
 )
 
-(allow mach-task-read
+(allow mach-task-name
 	(require-all
 		(system-attribute developer-mode)
 		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
 	)
 )
-(allow mach-task-read
+(allow mach-task-name
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.ts.mach-task-read")
 		(signing-identifier "com.apple.gputoolsserviced")

 	)
 )
 
-(allow mach-task-special-port*)
-
-(allow necp-client-open)
-
-(deny network*
+(deny necp-client-open
 	(require-all
 		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 	)
 )
-(deny network*
+(deny necp-client-open
 	(require-all
 		(literal "/private/var/tmp/ubiquity.socket")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 	)
 )
 
-(allow network-inbound
+(allow network*
 	(%entitlement-is-bool-true "com.apple.security.network.server")
 )
-(allow network-inbound
+(allow network*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any

 		)
 	)
 )
-(allow network-inbound
+(allow network*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.network.client")
 		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
 	)
 )
-(allow network-inbound
+(allow network*
 	(require-all
 		(extension "com.apple.sandbox.application-group")
 		(require-any

 		)
 	)
 )
-(deny network-inbound
+(deny network*
 	(require-all
 		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 	)
 )
-(deny network-inbound
+(deny network*
 	(require-all
 		(literal "/private/var/tmp/ubiquity.socket")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")

 )
 
 (allow network-bind
-	(%entitlement-is-bool-true "com.apple.security.network.server")
-)
-(allow network-bind
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			)
-			(require-all
-				(extension "com.apple.app-sandbox.read-write")
-				(require-any
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-				)
-			)
-			(require-all
-				(extension "com.apple.librarian.ubiquity-container")
-				(require-any
-					(require-all
-						(subpath "/private/var")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-						(subpath "${FRONT_USER_HOME}")
-					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				)
-			)
-		)
-	)
-)
-(allow network-bind
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.network.client")
-		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
-	)
-)
-(allow network-bind
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
-(deny network-bind
-	(require-all
-		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-	)
-)
-(deny network-bind
-	(require-all
-		(literal "/private/var/tmp/ubiquity.socket")
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-	)
-)
-
-(allow network-outbound
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 		(require-any

 		)
 	)
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(literal "/private/var/run/lockdown.sock")
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-client")
 	)
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(literal "/private/var/run/lockdown/checkin*")
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 	)
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any

 		)
 	)
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(extension "com.apple.sandbox.application-group")
 		(require-any

 		)
 	)
 )
-(allow network-outbound
+(allow network-bind
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.network.client")
 		(control-name "com.apple.flow-divert")
 	)
 )
-(deny network-outbound
+(deny network-bind
 	(require-all
 		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 	)
 )
-(deny network-outbound
+(deny network-bind
 	(require-all
 		(literal "/private/var/tmp/ubiquity.socket")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 	)
 )
 
-(allow nvram-delete
+(allow nvram*
 	(require-all
 		(nvram-variable "${ENTITLEMENT:com.apple.security.ts.nvram-delete}")
 		(%entitlement-is-present "com.apple.security.ts.nvram-delete")
 	)
 )
 
-(allow nvram-get
+(allow nvram-delete
 	(require-all
 		(nvram-variable "${ENTITLEMENT:com.apple.security.ts.nvram-read}")
 		(%entitlement-is-present "com.apple.security.ts.nvram-read")
 	)
 )
-(allow nvram-get
+(allow nvram-delete
 	(require-all
 		(nvram-variable "StartupMute")
 		(signing-identifier "com.apple.AccessibilityUIServer")
 	)
 )
-(allow nvram-get
+(allow nvram-delete
 	(require-all
 		(nvram-variable "boot-args")
 		(signing-identifier "com.apple.darwinaudiod")
 	)
 )
-(allow nvram-get
+(allow nvram-delete
 	(signing-identifier "com.apple.SoundBoard")
 )
-(allow nvram-get
+(allow nvram-delete
 	(require-all
 		(nvram-variable "${ENTITLEMENT:com.apple.security.ts.nvram-read-write}")
 		(%entitlement-is-present "com.apple.security.ts.nvram-read-write")
 	)
 )
 
-(allow nvram-set
+(allow nvram-get
 	(require-all
 		(nvram-variable "StartupMute")
 		(signing-identifier "com.apple.AccessibilityUIServer")
 	)
 )
-(allow nvram-set
+(allow nvram-get
 	(require-all
 		(nvram-variable "${ENTITLEMENT:com.apple.security.ts.nvram-read-write}")
 		(%entitlement-is-present "com.apple.security.ts.nvram-read-write")
 	)
 )
-(allow nvram-set
+(allow nvram-get
 	(require-all
 		(require-any
 			(nvram-variable "IONVRAM-FORCESYNCNOW-PROPERTY")

 	)
 )
 
-(allow process-codesigning)
+(allow process*)
+
+(allow process-codesigning
+	(with no-sandbox)
+	(require-all
+		(subpath "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework")
+		(system-attribute developer-mode)
+		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
+	)
+)
+(allow process-codesigning
+	(with no-sandbox)
+	(require-all
+		(system-attribute internal-build)
+		(system-attribute developer-mode)
+		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
+	)
+)
+(allow process-codesigning
+	(with no-sandbox)
+	(require-all
+		(process-path "/usr/libexec/thermalmonitord")
+		(system-attribute internal-build)
+	)
+)
 
 (allow process-exec*
 	(with no-sandbox)

 	)
 )
 
-(allow process-fork
+(allow process-exec-interpreter
 	(require-all
 		(system-attribute developer-mode)
 		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
 	)
 )
-(allow process-fork
+(allow process-exec-interpreter
 	(require-all
 		(process-path "/usr/libexec/thermalmonitord")
 		(system-attribute internal-build)
 	)
 )
 
-(allow process-info-codesignature)
-
-(allow process-info-dirtycontrol
+(allow process-info-codesignature
 	(require-all
 		(target others)
 		(system-attribute developer-mode)

 	)
 )
 
-(allow process-info-ledger
+(allow process-info-dirtycontrol
 	(signing-identifier "com.apple.dasd")
 )
 
-(allow process-info-pidinfo
+(allow process-info-listpids
 	(signing-identifier "com.apple.SoundBoard")
 )
 
-(allow process-info-sandbox-container
+(allow process-info-rusage
 	(require-any
 		(signing-identifier "com.apple.airplayd")
 		(signing-identifier "com.apple.fileindexerd")

 	)
 )
 
-(allow process-iopolicy*)
+(allow process-legacy-codesigning-entitlements-blob-get
+	(%entitlement-is-bool-true "com.apple.security.ts.get-code-signing-data")
+)
 
 (allow process-legacy-codesigning-entitlements-der-blob-get
 	(%entitlement-is-bool-true "com.apple.security.ts.get-code-signing-data")
 )
 
-(allow process-legacy-codesigning-identity-get
-	(%entitlement-is-bool-true "com.apple.security.ts.get-code-signing-data")
-)
-
-(allow process-legacy-codesigning-status-get
+(allow process-legacy-codesigning-status*
 	(%entitlement-is-bool-true "com.apple.security.ts.get-code-signing-data")
 )
 

 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
