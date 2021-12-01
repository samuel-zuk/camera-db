class Lens(db.Model):
    # Unique per-lens identifier string
    uuid = db.Column(db.String(36), unique=True, primary_key=True)

    # == Basic Meta Info ==
    # The common name of the lens (e.g. Canon EF 50mm f/1.8 STM)
    name = db.Column(db.String(120), nullable=False)
    # The brand of the lens (e.g. Nikon)
    brand = db.Column(db.String(40), nullable=False)
    # The lineup this lens is part of, if applicable (e.g. Sigma Art)
    lineup = db.Column(db.String(40))
    # The mount the lens was designed to be used on (e.g. Sony E)
    mount = db.Column(db.String(24))
    # The sensor size this lens was designed for (e.g. 4/3")
    lens_format = db.Column(db.String(12))
    # e.g. Dec 4, 1993
    release_date = db.Column(db.Date)
    # e.g. Japan
    origin_country = db.Column(db.String(32))
    # e.g. 1999.99
    msrp = db.Column(db.Float)
    # e.g. USD
    msrp_currency = db.Column(db.String(4))

    # == Focal Length ==
    # True if lens has a variable focal length
    is_zoom = db.Column(db.Boolean, nullable=False)
    # Focal length, expressed in mm (e.g. 70)
    # For zooms, this should be the lens's widest focal length.
    # For primes, this should be the lens's focal length.
    # Can support single-precision decimal focal lengths (e.g. 17.5)
    focal_length_min = db.Column(db.Numeric(6, 1), nullable=False)
    # Focal length, expressed in mm (e.g. 200).
    # For zooms, this should be the lens's longest focal length.
    # For primes, this field should be blank.
    # Can support single-precision decimal focal lengths (e.g. 17.5)
    focal_length_max = db.Column(db.Numeric(6, 1))
    
    # == Aperture ==
    # True if lens aperture is measured in T-stops rather than f-stops.
    uses_t_stops = db.Column(db.Boolean)
    # True if max lens aperture varies with focal length (for zooms).
    variable_aperture = db.Column(db.Boolean)
    # The maximum (widest) aperture of the lens (e.g. 1.7)
    # Can support double-precision decimal values (e.g. 0.95)
    aperture_max = db.Column(db.Numeric(4, 2), nullable=False)
    # The maximum (widest) aperture of a variable aperture zoom lens at
    #  the lens's longest focal length. (e.g. 2.8)
    # Can support double-precision decimal values (e.g. 0.95)
    aperture_v_max = db.Column(db.Numeric(4, 2)) 
    # The minimum (smallest) aperture of the lens (e.g. 22)
    # Can support single-precision decimal values (e.g. 11.4)
    aperture_min = db.Column(db.Numeric(3, 1))
    # True if lens has physical aperture ring
    has_aperture_ring = db.Column(db.Boolean)
    # True if aperture ring is mechanical (i.e. not electronic)
    mech_aperture_ring = db.Column(db.Boolean)
    # True if aperture ring is clickless or can be made to be clickless.
    declicked_aperture = db.Column(db.Boolean)

    # == Physical Lens Info ==
    # True if the lens has front filter threads.
    front_filters = db.Column(db.Boolean)
    # The filter thread of the lens, in mm (if applicable) (e.g. 58)
    # Can support single-precision decimal values (e.g. 42.5)
    filter_thread = db.Column(db.Numeric(4, 1))
    # The physical length of the lens, in mm (e.g. 55)
    # Can support single-precision decimal values (e.g. 102.7)
    length = db.Column(db.Numeric(4, 1))
    # The physical length of a zoom lens when fully extended, in mm (e.g. 58)
    # Can support single-precision decimal values (e.g. 102.7)
    length_v_max = db.Column(db.Numeric(4, 1))
    # The physical diameter of the lens, in mm (e.g. 49)
    # Can support single-precision decimal values (e.g. 34.4)
    diameter = db.Column(db.Numeric(4, 1))
    # The weight of the lens, in g (e.g. 1200)
    # Can support single-precision decimal values (e.g. 640.4)
    weight = db.Column(db.Numeric(6, 1))
    # True if lens is weather-resistant
    is_wr = db.Column(db.Boolean)
    # True if lens has a tripod foot collar.
    has_tripod_foot = db.Column(db.Boolean)

    # == Optical Information ==
    # The number of aperture diaphragm blades (e.g. 8)
    blades = db.Column(db.SmallInteger)
    # The number of optical elements in the lens (e.g. 7)
    elements = db.Column(db.SmallInteger)
    # The number of groups the lens's elements are in (e.g. 5)
    groups = db.Column(db.SmallInteger)
    # True if lens is a fisheye lens.
    is_fisheye = db.Column(db.Boolean)
    # True if lens is a mirror lens.
    is_mirror = db.Column(db.Boolean)

    # == Macro Information ==
    # The maximum magnification ratio 1:x (e.g. 1.5)
    # Can support double-precision decimal values (e.g. 1.75)
    mag_ratio = db.Column(db.Numeric(4, 2))
    # True if lens has a separate macro mode.
    has_macro_mode = db.Column(db.Boolean)

    # == Focusing Information ==
    # The minimum focusing distance, in cm (e.g. 10)
    # Can support single-precision decimal values (e.g. 20.5)
    close_focus = db.Column(db.Numeric(4, 1))
    # The longest minimum focusing distance of a zoom lens, in cm (e.g. 20)
    # Can support single-precision decimal values (e.g. 20.5)
    close_focus_v_max = db.Column(db.Numeric(4, 1))
    # True if lens is a parfocal zoom (maintains focus when zooming)
    is_parfocal = db.Column(db.Boolean)
    # True if lens is a varifocal zoom (loses focus when zooming)
    is_varifocal = db.Column(db.Boolean)
    # True if lens focuses by wire exclusively
    focus_by_wire = db.Column(db.Boolean)
    # True if lens focuses internally (i.e. doesn't extend)
    has_internal_focus = db.Column(db.Boolean)
    # True if front barrel rotates while focusing/zooming.
    has_rotating_barrel = db.Column(db.Boolean)
    # True if lens has autofocus.
    has_af = db.Column(db.Boolean)
    # True if lens has a physical AF/MF toggle.
    has_af_mf_toggle = db.Column(db.Boolean)
    # True if lens has a MF clutch (e.g. some M.Zuiko Pro lenses)
    has_mf_clutch = db.Column(db.Boolean)
    # True if lens has stops on the focusing ring for manual focus.
    has_mf_stops = db.Column(db.Boolean)
    # True if lens with MF stops has soft stops (e.g. many Nikon DSLR lenses)
    has_soft_stops = db.Column(db.Boolean)
    # True if lens has a focus range limiter.
    has_focus_limiter = db.Column(db.Boolean)

    # == Lens Features ==
    # True if lens has electronic connections (for AF, FBW, EXIF data, etc)
    is_electronic = db.Column(db.Boolean)
    # True if lens has image stabilization
    has_ois = db.Column(db.Boolean)
    # True if lens has a physical OIS toggle.
    has_ois_toggle = db.Column(db.Boolean)
    # True if lens has function button(s)
    has_fn_buttons = db.Column(db.Boolean)
    # The number of function buttons the lens has, if applicable
    fn_buttons = db.Column(db.SmallInteger)
    # True if lens has a programmable control ring (e.g. newer Canon lenses)
    has_ctrl_ring = db.Column(db.Boolean)
    # True if lens has an electonic display window (e.g. newer Nikon lenses)
    has_digital_display = db.Column(db.Boolean)
    # True if lens has geared control rings
    has_gears = db.Column(db.Boolean)
