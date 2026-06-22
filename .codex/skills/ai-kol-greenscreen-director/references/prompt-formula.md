# Prompt Formula

This reference defines the reusable prompt structure for the two image generations and the I2V prompt.

## Shared Visual Lock

Carry these traits from Step 1 into every later step:

- Same person and face.
- Same hairstyle.
- Same skin tone.
- Same age impression.
- Same football jersey / clothing.
- Same clean scene.
- Same lighting direction and color temperature.
- Same camera distance and lens feel.
- Same match-day mood.

## Step 1 Image Prompt: `first-frame.png`

Goal: pure talking-head first frame, no phone.

Formula:

```text
Create a photorealistic first frame for a Middle East football news app KOL talking-head ad.
Subject: [person].
Scene: [scene].
Format: [size].

The KOL faces camera, natural confident expression, realistic eyes, relaxed shoulders, subtle match-day energy.
Clean background, no background people, no clutter, no pillars.
No phone in frame.
No app logo, no corner bug, no stickers, no extra brand icons.
Camera focus is on the face, natural depth of field, realistic indoor/outdoor lighting based on the scene.
High-quality commercial video still, ready for image-to-video generation.
```

Step 1 negative prompt:

```text
phone, smartphone, green screen phone, app logo, watermark, corner logo, sticker, text overlay, background people, crowd behind subject, clutter, pillars, messy room, extra hands, distorted fingers, stiff expression, robotic face, dead eyes, frozen face, low quality, blurry face
```

## Step 2 Image Prompt: `phone-reference.png`

Goal: generate the phone reference from `first-frame.png`.

Use `first-frame.png` as the primary reference image. The only new action is raising a phone into the foreground.

Formula:

```text
Using first-frame.png as the main reference, create a second photorealistic frame of the same KOL in the exact same scene.

Preserve the same face, hairstyle, skin tone, age impression, jersey/clothing, background, lighting, camera distance, and match-day mood.
Only add the action: the KOL raises a smartphone toward the camera.

The smartphone is in the foreground and occupies about 70% of the frame.
The phone screen is pure chroma key green, evenly lit, with no UI, no text, no logo, and no reflections covering the green.
Rack focus to the phone: the phone body and green screen are sharp and clear.
The KOL and background are visibly blurred with shallow depth of field.
Commercial video reference frame, realistic hand pose, clean composition.
```

Step 2 negative prompt:

```text
different person, changed face, changed hairstyle, changed skin tone, changed jersey, changed scene, changed lighting, changed camera distance, app UI on phone, logo on phone, text on phone, non-green phone screen, reflections blocking green screen, blurry phone, blurry green screen, sharp background, sharp face, background people, clutter, pillars, extra brand icons, extra fingers, distorted hand
```

## Step 3 I2V Prompt

Goal: transform the two stills into a video direction prompt.

Formula:

```text
Create a [duration]-second photorealistic KOL talking-head video for a Middle East football news app.
Use first-frame.png as the opening visual identity reference and phone-reference.png as the phone/rack-focus reference.

0-10s:
The KOL speaks directly to camera about football match-day pain points and emotions: waiting for lineups, trying to understand formations, checking match status, and following important teams and leagues.
Natural blinking, breathing, slight nods, moderate speaking pace, real KOL delivery.
Camera focus stays on the face.

10s-[duration]:
The KOL introduces the football app features: starting lineups, formation analysis, END, Delayed, ABD, CAN status labels, follow up to 5 teams, follow up to 5 competitions/leagues, and a customized score homepage.
Then the KOL raises a smartphone toward camera.
Rack focus shifts from the face to the phone.
The phone fills about 70% of the frame, with a pure chroma key green screen, sharp and clear.
The KOL and background become visibly blurred with shallow depth of field.

Keep the same person, clothing, scene, lighting, and camera distance throughout.
No app logo, no corner bug, no stickers, no extra brand icons.
Clean background with no people, clutter, or pillars.
```

I2V negative prompt:

```text
identity drift, changing face, changing jersey, changing background, stiff expression, robotic delivery, dead eyes, frozen face, unnatural blinking, lip sync errors, background people, clutter, pillars, app logo, watermark, corner bug, text overlay, phone UI, non-green phone screen, blurry phone screen, distorted hands, extra fingers, camera shake, low quality
```

## Feature Checklist

Every final script and I2V prompt must include:

- Starting lineups.
- Formation analysis.
- `END`.
- `Delayed`.
- `ABD`.
- `CAN`.
- Follow up to 5 teams.
- Follow up to 5 competitions / leagues.
- Customized score homepage.
