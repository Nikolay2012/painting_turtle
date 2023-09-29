import modules.input_data as m_data
import modules.settings as m_settings

m_settings.pen1.forward(m_data.step)
m_settings.pen1.left(m_data.turn_angle)
m_settings.pen1.forward(m_data.step)